import sqlite3
import pandas as pd
from functools import wraps

def check_connection(func):
    """Decorator to check if the database connection is established."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.db_connect():
            return func(self, *args, **kwargs)
        else:
            raise ConnectionError("Failed to connect to the database.")
    return wrapper

class SchoolDatabase:
    def __init__(self, db_path: str):
        self.db_path = db_path
        
    def db_connect(self):
        """
        Creates a connection to the SQLite database.

        Parameters:
        db_path (str): Path to the SQLite database file.

        Returns:
        sqlite3.Connection: A connection object to the database.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            print("Database connection successful.")
            return conn
        except sqlite3.Error as e:
            print(f'Database connection failed: {e}')
            return None
    
    def load_data_to_sqlite(self, data_url: str, table_name: str) -> None:
        """
        Loads data from a CSV URL into an SQLite table.

        Parameters:
        db_path (str): Path to the SQLite database file.
        data_url (str): URL to the CSV data.
        table_name (str): Name of the table to create or replace in the SQLite database.
        """
        conn = None
        try:
            conn = self.db_connect()
            df = pd.read_csv(data_url)
            df.to_sql(table_name, conn, index=False, if_exists='replace')
            print(f"Data loaded successfully into '{table_name}' table.")
        except sqlite3.Error as e:
            print(f"An error occurred while loading data into '{table_name}': {e}")
        finally:
            if conn:
                conn.close()
        
    def get_table_names(self) -> list:
        """
        Retrieves a list of all table names in the SQLite database.

        Parameters:
        db_path (str): Path to the SQLite database file.

        Returns:
        list: A list of table names.
        """
        conn = None
        try:
            conn = self.db_connect()
            cursor = conn.cursor()
            cursor.execute('SELECT name from sqlite_master where type="table"')
            tables = cursor.fetchall()
            print("Table names retrieved successfully")
            return tables
        except sqlite3.Error as e:
            print(f"Failed to retrieve table names: {e}")
        finally:
            if conn:
                conn.close()
    
    def get_table_info(self, table_name: str) -> list:
        """
        Retrieves the schema information of a given table.

        Parameters:
        db_path (str): Path to the SQLite database file.
        table_name (str): Name of the table to retrieve information for.

        Returns:
        list: A list of tuples containing the schema information.
        """

        conn = None
        try:
            conn = self.db_connect()
            cursor = conn.cursor()
            cursor.execute(f'PRAGMA table_info({table_name})')
            info = cursor.fetchall()
            print(f"Table info for '{table_name}' retrieved successfully.")
            return info
        except sqlite3.Error as e:
            print(f"An error occurred while retrieving info for '{table_name}': {e}")
        finally:
            if conn:
                conn.close()
                
    def run_query(self, statement: str) -> list:
        """
        Executes a SQL statement and returns the results.

        Parameters:
        db_path (str): Path to the SQLite database file.
        statement (str): SQL statement to execute.

        Returns:
        list: A list of tuples containing the query results.
        """
        conn = None
        try:
            conn = self.db_connect()
            cursor = conn.cursor()
            cursor.execute(statement)
            results = cursor.fetchall()
            print("Query executed successfully.")
            return results
        except sqlite3.Error as e:
            print(f"An error occurred while executing the query: {e}")
        finally:
            if conn:
                conn.close()

    def get_difference_between_students_and_test_takers(self) -> list[type]:
        """Calculates the difference between total students and number of test takers for each boro."""
        statement = """
        SELECT 
          hs.boro,
          SUM(hs.total_students) - SUM(sr.num_test_takers) AS difference
        FROM 
          high_schools hs
        JOIN 
          sat_records sr ON hs.dbn = sr.dbn
        GROUP BY 
          hs.boro
        ORDER BY 
          difference ASC;
        """
        try:
            results = self.run_query(statement)
            print("Successfully retrieved the difference between total students and number of test takers for each boro.")
            return results
        except Exception as e:
            print(f"An error occurred while calculating the difference: {e}")
            return []
import sys
import os
import unittest
import sqlite3

import unittest
from HtmlTestRunner import HTMLTestRunner

project_root = os.path.abspath(os.path.join(os.getcwd(), '../'))
sys.path.insert(0, project_root)

from dev.school_database_dev import SchoolDatabase

class TestSchoolDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # This runs once before all tests
        cls.db_path = 'test_schools.db'  # Use a test database path
        cls.school_db = SchoolDatabase(cls.db_path)

    def test_database_connection(self):
        """Test if the database connection is established successfully."""
        conn = self.school_db.db_connect()
        self.assertIsInstance(conn, sqlite3.Connection)
 
    def test_load_data_to_sqlite(self):
            """Test if data is loaded into the database correctly."""
            # You would need a test CSV file for this
            test_csv_url = 'https://raw.githubusercontent.com/sql-fundamentals-jigsaw/mod-1-sql-curriculum/master/2-sql-relations/2-belongs-to-hs/data/highschools.csv'
            self.school_db.load_data_to_sqlite(test_csv_url, 'high_schools')
            # Verify that the table now exists in the database
            tables = self.school_db.get_table_names()
            self.assertIn('high_schools', [table[0] for table in tables])

    def test_get_table_names(self):
        """Test if table names are retrieved correctly."""
        tables = self.school_db.get_table_names()
        self.assertIsInstance(tables, list)

    def test_high_schools_count(self):
        """Test if high_schools table is equal to 427."""
        result = self.school_db.run_query('SELECT COUNT(*) FROM high_schools')[0][0]
        self.assertEqual(427, result)

    def test_boro_are_complete(self):
        """Test if any boro is missing."""
        results = self.school_db.run_query('SELECT DISTINCT boro FROM high_schools')
        final_results = [boro[0] for boro in results ]
        self.assertEqual(['K', 'M', 'Q', 'X', 'R'], final_results)

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestSchoolDatabase)
    test_runner = HTMLTestRunner(output='test_reports', report_name='product_test_report', combine_reports=True)
    test_runner.run(test_suite)
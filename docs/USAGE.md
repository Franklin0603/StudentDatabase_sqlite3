# StudentDatabase Documentation

## Overview

The `StudentDatabase` project is designed to manage and analyze educational data through a Python interface to an SQLite database. It provides tools for loading data, querying records, and performing data analysis on student and school performance metrics.

## Getting Started

### Prerequisites

- Python 3.x
- SQLite3
- Pandas library
- Jupyter Notebook (for `.ipynb` files)

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/StudentDatabase.git
cd StudentDatabase
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Setting Up the Database
To set up the database, run the preprocessing.ipynb notebook in the ws/clean/ directory. This will load the initial data into the SQLite database.

## Usage
### Loading Data
To load data into the database, use the load_data_to_sqlite function from the school_database.py script in the dev/ or prod/ directory.

## How to use it 

### Querying Data
Use the `run_query` function to execute SQL queries against the database. Example queries can be found in the `usage_guide.ipynb` notebook in the `docs/` directory. The `usage_guide.ipynb` directory contains Jupyter notebooks that demonstrate typical use cases and data analysis workflows.

## Testing
Instructions on how to run the test suite located in the `tests/` directory.
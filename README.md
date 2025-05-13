# SQL + Python Data Access Demo Project

This project demonstrates how to securely connect a Python script to a Neon-hosted PostgreSQL database using environment variables and SQLAlchemy.

## Features

-  Environment-based credential handling via a .env file
-  SQLAlchemy connection setup to a remote PostgreSQL server
-  Executing SQL queries and loading results into a pandas DataFrame
-  Sample table creation and mock data insertion for testing
-  Organized Python structure with reusable database utilities

## Tech Stack

- Python 3.11+
- PostgreSQL (Neon)
- SQLAlchemy
- psycopg2-binary
- python-dotenv
- pandas

## Usage

Run the main script:
```bash
python main.py
```

This will:
1. Create a sample table if it doesn't exist
2. Insert some test data
3. Execute a sample query
4. Display the results and some basic statistics

## Project Structure

- `main.py`: Main script demonstrating database operations
- `db_utils.py`: Database utility functions and connection handling
- `requirements.txt`: Project dependencies
- `.env`: Database credentials (not tracked in git)
- `.env.example`: Template for the .env file

## Security Notes

- Never commit the `.env` file to version control
- Keep your database credentials secure
- Use environment variables for sensitive information 
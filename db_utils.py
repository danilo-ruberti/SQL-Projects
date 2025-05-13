import os
from typing import Optional
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_db_connection() -> Engine:
    """
    Create and return a SQLAlchemy database engine using environment variables.
    Returns:Engine: SQLAlchemy engine instance
    """
    db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}?sslmode=require"
    return create_engine(db_url)

def execute_query(query: str, params: Optional[dict] = None) -> pd.DataFrame:
    """
    Execute a SQL query and return results as a pandas DataFrame.
    
    Args:
        query (str): SQL query to execute
        params (dict, optional): Query parameters
    Returns: pd.DataFrame: Query results
    """
    engine = get_db_connection()
    with engine.connect() as connection:
        result = connection.execute(text(query), params or {})
        # Convert result keys to list to fix the DataFrame creation issue
        columns = list(result.keys())
        return pd.DataFrame(result.fetchall(), columns=columns)

def create_sample_table():
    """
    Create a sample table with mock data for testing purposes.
    """
    engine = get_db_connection()
    
    # Create sample table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS sample_data (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        value INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    
    # Insert sample data
    insert_data_query = """
    INSERT INTO sample_data (name, value) VALUES
    ('Alpha Widget', 120),
    ('Beta Gadget', 340),
    ('Gamma Tool', 275),
    ('Delta Device', 430),
    ('Epsilon Gear', 150),
    ('Zeta Instrument', 390),
    ('Eta Apparatus', 210),
    ('Theta Machine', 310),
    ('Iota Module', 490),
    ('Kappa Engine', 305);
    """
    
    with engine.connect() as connection:
        connection.execute(text(create_table_query))
        connection.execute(text(insert_data_query))
        connection.commit() 
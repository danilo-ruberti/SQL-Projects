from db_utils import execute_query, create_sample_table

def main():
    # NOTE: Uncomment the following line only for the first run to create and populate the table
    # After the first run, keep it commented to avoid duplicate data
    # create_sample_table()
    
    # Execute a sample query
    print("\nExecuting sample query...")
    query = "SELECT * FROM sample_data ORDER BY value DESC"
    df = execute_query(query)
    
    # Display results
    print("\nQuery Results:")
    print(df)
    
    # Display some basic statistics
    print("\nBasic Statistics:")
    print(f"Total records: {len(df)}")
    print(f"Average value: {df['value'].mean():.2f}")
    print(f"Min value: {df['value'].min()}")
    print(f"Max value: {df['value'].max()}")
    
    # Display value distribution
    print("\nValue Distribution:")
    print(df['value'].describe())

if __name__ == "__main__":
    main() 
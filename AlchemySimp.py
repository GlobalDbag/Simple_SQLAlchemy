from sqlalchemy import create_engine, MetaData, Table, select

# Get the connection string from the user
connection_string = "mysql+pymysql://username:password@localhost/database"

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

# Get the database metadata
metadata = MetaData(bind=engine)
metadata.reflect()

# Get all tables in the database
table_names = metadata.tables.keys()

# Print the data from each table
for table_name in table_names:
    # Get the table object
    table = Table(table_name, metadata, autoload=True)

    # Create a select query for the table
    select_query = select([table])

    # Execute the query and fetch all rows
    with engine.connect() as connection:
        result = connection.execute(select_query)
        rows = result.fetchall()

    # Print the table name
    print(f"Data from table '{table_name}':")

    # Print each row
    for row in rows:
        print(row)

    # Print a separator between tables
    print("-" * 50)

import psycopg2
from psycopg2 import Error

def connect_to_database():
    try:
        # Establish connection to PostgreSQL database
        connection = psycopg2.connect(
            database="prueba",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Print PostgreSQL Connection properties
        print("PostgreSQL server information:")
        print(connection.get_dsn_parameters())
        
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

        return connection, cursor

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None, None

def close_connection(connection, cursor):
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

if __name__ == "__main__":
    # Test the connection
    connection, cursor = connect_to_database()
    if connection:
        close_connection(connection, cursor) 
import mysql.connector
from mysql.connector import Error

# Function to establish a connection to MySQL
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='your_db',
            user='your_user',
            password='your_password'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    return None

# 1. CREATE (Insert)
def create_record(connection):
    try:
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO your_table_name (column1, column2, column3)
        VALUES (%s, %s, %s)
        """
        values = ('value1', 'value2', 'value3')
        cursor.execute(insert_query, values)
        connection.commit()
        print(f"Record inserted successfully, ID: {cursor.lastrowid}")
    except Error as e:
        print(f"Error while inserting: {e}")

# 2. READ (Select)
def read_records(connection):
    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM your_table_name"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error while reading: {e}")

# 3. UPDATE
def update_record(connection):
    try:
        cursor = connection.cursor()
        update_query = """
        UPDATE your_table_name
        SET column1 = %s, column2 = %s
        WHERE id = %s
        """
        values = ('new_value1', 'new_value2', 1)  # Assuming 'id' is the primary key
        cursor.execute(update_query, values)
        connection.commit()
        print(f"Record updated successfully, Rows affected: {cursor.rowcount}")
    except Error as e:
        print(f"Error while updating: {e}")

# 4. DELETE
def delete_record(connection):
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM your_table_name WHERE id = %s"
        value = (1,)  # Assuming 'id' is the primary key
        cursor.execute(delete_query, value)
        connection.commit()
        print(f"Record deleted successfully, Rows affected: {cursor.rowcount}")
    except Error as e:
        print(f"Error while deleting: {e}")

# Main function to execute all CRUD operations
def main():
    connection = connect_to_mysql()
    if connection:
        try:
            # Call the CRUD functions here
            print("Create Operation:")
            create_record(connection)
            
            print("\nRead Operation:")
            read_records(connection)

            print("\nUpdate Operation:")
            update_record(connection)

            print("\nDelete Operation:")
            delete_record(connection)

        finally:
            # Close the connection
            if connection.is_connected():
                connection.close()
                print("\nMySQL connection is closed")

if __name__ == '__main__':
    main()

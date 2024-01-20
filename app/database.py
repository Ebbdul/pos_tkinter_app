# database.py
import mysql.connector

# Your database connection details
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "123@abc"
DB_NAME = "pos"

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def validate_credentials(username, password):
    connection = connect_to_database()

    if connection:
        try:
            cursor = connection.cursor()
            # Execute a query to check if the username and password match
            query = "SELECT * FROM user WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))

            # Fetch the result
            result = cursor.fetchone()

            # If result is not None, the credentials are valid
            return result is not None

        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")
            return False

        finally:
            # Close the cursor and connection in the finally block to ensure they're always closed
            cursor.close()
            connection.close()

    else:
        # Return False if the connection couldn't be established
        return False

def fetch_data():
    connection = connect_to_database()

    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM patient_data"
            cursor.execute(query)
            data = cursor.fetchall()
            # print(data)
            return data

        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")
            return []

        finally:
            cursor.close()
            connection.close()

    else:
        # Return an empty list if the connection couldn't be established
        return []

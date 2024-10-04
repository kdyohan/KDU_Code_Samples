from flask import Flask, render_template, request, redirect
import mysql.connector
from mysql.connector import Error

# Create the Flask application instance
app = Flask(__name__)
connection = mysql.connector.connect(
            host='localhost',      # Hostname of the server
            database='restaurant_app',    # Database name
            port = 3306,
            user='root',      # Username
            password='9548@Yohan'  # Password for the user
            
        )
def connect_to_mysql():
    try:
        # Establish a connection to the MySQL server        
        if connection.is_connected():
            print("Successfully connected to the MySQL database")
            # You can execute your queries here
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()
            print(f"You're connected to the database: {db_name}")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    # finally:
    #     if connection.is_connected():
    #         cursor.close()
    #         connection.close()
    #         print("MySQL connection is closed")
            
            
# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        connect_to_mysql()
        if connection.is_connected():
            
           connection.cursor() 
           connection.close()
           print("MySQL connection is closed") 
        return f'Hello, {name}! We have received your email: {email}'

if __name__ == '__main__':
    app.run(debug=True)
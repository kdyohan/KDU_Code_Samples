from flask import Flask, render_template, request, redirect
import mysql.connector

# Initialize Flask app
app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_user",
    password="your_mysql_password",
    database="flask_crud_db"
)
cursor = db.cursor()

# Home route (Read data)
@app.route('/')
def index():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template('index.html', students=students)

# Route to show create form
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        
        cursor.execute("INSERT INTO students (name, age, city) VALUES (%s, %s, %s)", (name, age, city))
        db.commit()
        return redirect('/')
    return render_template('create.html')

# Route to update a student
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cursor.fetchone()

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        
        cursor.execute("UPDATE students SET name=%s, age=%s, city=%s WHERE id=%s", (name, age, city, id))
        db.commit()
        return redirect('/')
    
    return render_template('update.html', student=student)

# Route to delete a student
@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

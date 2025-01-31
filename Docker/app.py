from flask import Flask, request, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/')
def home():
    # Render an HTML form for user input
    return render_template('index.html')

@app.route('/connect', methods=['POST'])
def connect_to_database():
    try:
        # Get database credentials from the form
        host = request.form.get('host')
        user = request.form.get('user')
        password = request.form.get('password')
        database = request.form.get('database')

        # Connect to the database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            return f"""
                <h3>✅ Connected to the database successfully!</h3>
                <p><b>Host:</b> {host}</p>
                <p><b>User:</b> {user}</p>
                <p><b>Database:</b> {database}</p>
                <a href="/">Go back</a>
            """

    except Error as e:
        return f"""
            <h3>❌ Error connecting to database:</h3>
            <p>{str(e)}</p>
            <a href="/">Go back</a>
        """

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

# Configuration for connecting to the database
server = 'your_server_name'
database = 'dev_database.sql'
username = 'your_username'
password = 'your_password'
driver = '{ODBC Driver 17 for SQL Server}'

# API endpoint for processing the data
@app.route('/process', methods=['POST'])
def process_data():
    try:
        # Retrieve the data from the request
        data = request.get_json()
        text = data['text']

        # Store the data in the database or perform any desired processing
        # Here, we'll just return the processed text
        processed_text = text.upper()

        return jsonify({'result': processed_text})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()

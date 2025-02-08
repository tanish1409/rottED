from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os
import sys

app = Flask(__name__)
CORS(app)


@app.route('/process_pdf', methods=['POST'])
def process_pdf():
    file = request.files['file']
    if file:
        file_path = os.path.join("uploads", file.filename)
        os.makedirs("uploads", exist_ok=True)
        file.save(file_path)

        # result = subprocess.run(['python', 'main.py', file_path], capture_output=True, text=True)
        # result = subprocess.run(
        #    ['C:/Users/kunal/OneDrive/Desktop/Hackathon/test/venv/Scripts/python.exe', 'main.py', file_path],
        #    capture_output=True, text=True)

        python_executable = sys.executable
        result = subprocess.run([python_executable, 'main.py', file_path], capture_output=True, text=True)
        if result.returncode == 0:
            return jsonify({'message': 'PDF processed successfully', 'output': result.stdout})
        else:
            return jsonify({'error': result.stderr}), 500

    return jsonify({'error': 'No file uploaded'}), 400


if __name__ == '__main__':
    app.run(debug=True)

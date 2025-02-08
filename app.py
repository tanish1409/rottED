from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import subprocess
import os
import sys
import uuid
import shutil

app = Flask(__name__)
CORS(app)

STATIC_FOLDER = 'static'  # Folder to store generated videos
os.makedirs(STATIC_FOLDER, exist_ok=True)


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
            unique_id = str(uuid.uuid4())
            output_video_filename = f'output_{unique_id}.mp4'
            output_video_path = os.path.join(STATIC_FOLDER, output_video_filename)
            print(output_video_path)
            try:
                shutil.copy('final_output.mp4', output_video_path)
            except Exception as e:
                print(f"An error occurred while generating video: {e}")
            return jsonify({'message': 'PDF processed successfully', 'output': result.stdout})
        else:
            return jsonify({'error': result.stderr}), 500

    return jsonify({'error': 'No file uploaded'}), 400


if __name__ == '__main__':
    app.run(debug=True)

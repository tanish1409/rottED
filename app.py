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

video_urls = []


@app.route('/process_pdf', methods=['POST'])
def process_pdf():
    file = request.files['file']
    brainrot_mode = request.form.get('brainrot_mode')  # Get BrainRot status
    print("BRAINROT MODE: " + brainrot_mode)
    if file:
        file_path = os.path.join("uploads", file.filename)
        os.makedirs("uploads", exist_ok=True)
        file.save(file_path)

        python_executable = sys.executable
        result = subprocess.run([python_executable, 'main.py', file_path, brainrot_mode], capture_output=True, text=True)
        print("Subprocess STDOUT:", result.stdout)
        if result.returncode == 0:
            unique_id = str(uuid.uuid4())
            output_video_filename = f'output_{unique_id}.mp4'
            output_video_path = os.path.join(STATIC_FOLDER, output_video_filename)
            video_url = f'./../../../static/{output_video_filename}'
            video_urls.append(video_url)
            print(video_urls)
            try:
                shutil.copy('final_output.mp4', output_video_path)
            except Exception as e:
                print(f"An error occurred while generating video: {e}")
            return jsonify({'message': 'PDF processed successfully', 'output': result.stdout, 'video_urls': video_urls})
        else:
            return jsonify({'error': result.stderr}), 500

    return jsonify({'error': 'No file uploaded'}), 400


if __name__ == '__main__':
    app.run(debug=True)

import os
import subprocess
import cv2
import numpy as np
from flask import Flask, request, jsonify, render_template, send_file
from flask import send_file


app = Flask(__name__)

# Define the path to the 'inference_realesrgan.py' script within the REAL-ESRGAN folder
real_esrgan_script_path = os.path.join('Real-ESRGAN', 'inference_realesrgan.py')


@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/enhance_image', methods=['POST'])
def enhance_image():
    # Check if an image file is provided
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    # Load the uploaded image
    uploaded_image = request.files['image']
    input_image_path = 'uploads/input.png'
    uploaded_image.save(input_image_path)


  

    # Define the Real-ESRGAN command
    real_esrgan_command = [
        'python', real_esrgan_script_path,
        '-n', 'RealESRGAN_x4plus',
        '-i', input_image_path,
        '-o', 'static',
        '--outscale', '3.5',
        '--face_enhance',
        '--fp32',
        '-t', '512'
    ]

    try:
        # Run the Real-ESRGAN script to enhance the image
        subprocess.run(real_esrgan_command, check=True)
    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)}), 500

    # Get the name of the enhanced image file
    enhanced_image_filename = 'static/input_out.png'

    # Pass the enhanced image filename to the result template
    return render_template('result.html', enhanced_image_filename=enhanced_image_filename)

@app.route('/download_enhanced_image')
def download_enhanced_image():
    # Define the path to the enhanced image
    enhanced_image_path = 'static/input_out.png'
    
    # Return the enhanced image as a downloadable attachment
    return send_file(enhanced_image_path, as_attachment=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)     
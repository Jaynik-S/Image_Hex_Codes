from flask import Flask, request, render_template
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_page():
    return render_template('upload_page.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return 'No file uploaded!', 400

    file = request.files['image']
    if file.filename == '':
        return 'No selected file!', 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Process the image with a default step size
    hex_table = process_image(filepath, step=5)

    return render_template('hex_table.html', table=hex_table, image_path=filepath, step=5)

@app.route('/process', methods=['POST'])
def process_with_step():
    step = int(request.form.get('step', 5))
    image_path = request.form.get('image_path')

    # Ensure the file exists before processing
    if not os.path.exists(image_path):
        return "Image file not found! Please re-upload.", 400

    # Process the image with the specified step size
    hex_table = process_image(image_path, step)

    return render_template('hex_table.html', table=hex_table, image_path=image_path, step=step)

def process_image(filepath, step):
    image = Image.open(filepath).convert('RGB')
    width, height = image.size

    hex_table = []
    for y in range(0, height, step):
        row = []
        for x in range(0, width, step):
            pixel = image.getpixel((x, y))
            hex_code = '#{:02x}{:02x}{:02x}'.format(pixel[0], pixel[1], pixel[2])
            row.append(hex_code)
        hex_table.append(row)

    return hex_table

if __name__ == '__main__':
    app.run(debug=True)

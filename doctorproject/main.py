from PIL import Image
from io import BytesIO

def convert_png_to_jpg(file):
    png_image = Image.open(file)
    jpg_image = png_image.convert('RGB')
    with BytesIO() as output:
        jpg_image.save(output, format='JPEG', quality=95)
        return output.getvalue()
    
#flask code
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            jpg_data = convert_png_to_jpg(file)
            return Response(jpg_data, mimetype='image/jpeg')
    return render_template('index.html')

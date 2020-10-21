import imghdr
import os
from skimage import data, io
from skimage.color import rgb2gray
from flask import Flask, render_template, request, redirect, url_for, abort, send_file
from werkzeug.utils import secure_filename
    
app=Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


# Create a directory in a known location to save files to.
uploads_dir = os.path.join(app.instance_path, 'uploads')

if not os.path.exists('./instance/uploads'):
    os.makedirs(uploads_dir)

@app.route("/")
def home():
    return render_template('app.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    try:
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS'] or file_ext != validate_image(uploaded_file.stream):
                abort(400)
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))

        filestring = "./uploads/" + filename
        filename = os.path.join(filestring)
        original = io.imread(filename)
        grayscale = rgb2gray(original)

        io.imsave('result.jpg', grayscale)

        return send_file('./result.jpg', attachment_filename='result.jpg')
        
    except Exception as e:
        return render_template('app.html', results=str(e))

#Main method
if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True, threaded=True)
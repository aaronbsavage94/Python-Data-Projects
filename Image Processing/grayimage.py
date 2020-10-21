import imghdr
import os
from skimage import data, io
from skimage.color import rgb2gray
from flask import Flask, render_template, request, redirect, url_for, abort, send_file
from werkzeug.utils import secure_filename

#Config
app=Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'

#Image validation
def validate_image(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


# Create upload directory
uploads_dir = os.path.join(app.instance_path, 'uploads')

#If it does not exist already, create it
if not os.path.exists('./instance/uploads'):
    os.makedirs(uploads_dir)

#Render main page
@app.route("/")
def home():
    return render_template('app.html')

#Upload method
@app.route('/upload', methods=['GET', 'POST'])
def upload():

    try:
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)

        #If the file is not null
        if filename != '':
            file_ext = os.path.splitext(filename)[1]

            #If we fail the validation tests, throw a 400
            if file_ext not in app.config['UPLOAD_EXTENSIONS'] or file_ext != validate_image(uploaded_file.stream):
                abort(400)
            
            #Save uploaded file to directory
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))

        #Concatenate file path
        filestring = "./uploads/" + filename
        filename = os.path.join(filestring)
        original = io.imread(filename)

        #Rgb2gray
        grayscale = rgb2gray(original)

        #Save the result
        io.imsave('result.jpg', grayscale)

        #Return the resulting file
        return send_file('./result.jpg', attachment_filename='result.jpg')

    #Return the exception and append the exception details to the HTML
    except Exception as e:
        return render_template('app.html', results=str(e))

#Main method
if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True)
from flask import Flask, flash, jsonify, render_template, request, redirect, url_for
import service.captiongen as capgen, os

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = 'static/'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        print("Not found")
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    print("Get DIr: ", dir(file))
    print(file.content_type)
    print(file.filename)
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # return render_template('index.html', filename=filename)
        
        caption = capgen.generateCaption(filename)
        
        return render_template('index.html', filename=filename, caption=caption)
        

if __name__ == '__main__':
    app.run(debug=True)
import joblib
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def upload_page():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
    #   f.save(secure_filename(f.filename))
      f.save(f"New folder/{f.filename}")   # can be save by both ways
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)
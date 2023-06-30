from flask import Flask, request, render_template
from decode import *

app = Flask(__name__)



from flask import render_template

@app.route('/')
def main(name=None):
   return render_template('index.html', name=name)

@app.route('/success',methods = ['POST'])
def success(): 
   if request.method == 'POST':  
      f = request.files['file']
      decode_file_content(f)
      return render_template("success.html", name = f.filename)  



from flask import Flask,make_response,url_for,redirect,request, render_template
from decode import *

app = Flask(__name__)



from flask import render_template



@app.errorhandler(404)
def not_found(error):
   return render_template('error.html'), 404


@app.route('/')
def main():
   return render_template('index.html')


@app.route('/success',methods = ['GET'])
def success():
   response = make_response(render_template('success.html'),200)
   return response

@app.route('/sending',methods = ['POST','GET'])
def jsonReceived():
   if request.method == 'POST':
      r = request.json
      decode_file_content(r)
      return redirect(url_for("success"))
   return redirect(url_for("not_found"))
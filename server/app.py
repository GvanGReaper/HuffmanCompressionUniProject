from flask import Flask,make_response,url_for,redirect,request, render_template
from decode import *

app = Flask(__name__)


@app.route("/",methods=['POST','GET'])
def main():
   return render_template("index.html")


@app.route("/pleaseWait",methods = ['POST','GET']) 
def answers_submitted():
   if request.method == 'POST':
      data = request.form
      print(data)
   return render_template("success.html")


if __name__ == "__main__":
   app.run()
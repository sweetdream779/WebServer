from flask import Flask, request, render_template, send_from_directory
import os
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=='POST':
        return render_template("complete.html")
    else equest.method=='GET':
        return render_template("upload.html")

@app.route("/complete", methods=["POST"])
def upload():
    return render_template("complete.html")

if __name__ == '__main__':
  app.run(debug=True)

from flask import Flask, request, render_template, send_from_directory
import os
from PIL import Image
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=='POST':
        im = Image.open("images/bg.jpg")
        return render_template("complete.html")
    return render_template("upload.html")

if __name__ == '__main__':
  app.run(debug=True)

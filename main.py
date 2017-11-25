from flask import Flask, request, render_template, send_from_directory
import os
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    return render_template("complete.html", size=0)

if __name__ == '__main__':
  app.run()

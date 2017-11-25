from flask import Flask, request, render_template, send_from_directory
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("upload.html")

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == '__main__':
  app.run()

from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=='POST':
        f = request.files['file']
        return render_template("complete.html")
    return render_template("upload.html")

if __name__ == '__main__':
  app.run(debug=True)

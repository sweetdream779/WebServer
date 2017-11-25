from flask import Flask, request, render_template, send_from_directory
import urllib
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=='POST':
        #im = Image.open("images/bg.jpg")
        os.mkdir('dir')
        with open('dir/text.txt','w') as f:
            f.write('jljl/r/n')
        with open('dir/text.txt','r') as f:
            s=f.readline()
        return render_template("complete.html", str=s)
    return render_template("upload.html")

if __name__ == '__main__':
  app.run(debug=True)

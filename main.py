from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

def count_words(file):
    pass


def count_chars(file):
    pass


@app.route("/",methods=["GET","POST"])
def index():
    if request.method=='POST':
        f = request.files['file']
        i=0
        for line in f:
            s=f.readline()
            i+=1
            if 2==1:
                break
        return render_template("complete.html",text=s)
    return render_template("upload.html")

if __name__ == '__main__':
  app.run(debug=True)

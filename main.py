from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

def count_words(file):
    i=0
    for line in f:
        s=f.readline()[:-1]
        words=s.split(' ')
        i+=len(words)
    return i


def count_chars(file):
    pass


def count_lines(file):
    i=0
    for line in f:
        s=f.readline()
        i+=1
    return i


@app.route("/",methods=["GET","POST"])
def index():
    if request.method=='POST':
        file = request.files['file']
        lines=str(count_lines(file))
        words=str(count_words(file))
        return render_template("complete.html",lines=lines,words=words)
    return render_template("upload.html")

if __name__ == '__main__':
  app.run(debug=True)

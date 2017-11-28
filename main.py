from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

def count_words_chars_lines(file):
    lines_count=0
    words_count=0
    chars_count=0
    existWords=[]
    d=", "
    for line in file:
        line=line.decode()
        if(len(line.split('\n'))>1):
            line=line.split('\n')[0]
        else:
            line=line.split('\r\n')[0]
        chars_count+=len(line)
        words_count+=wordCount(line,existWords)
        lines_count+=1
    str_words=d.join(existWords)
    return [str(words_count), str(chars_count), str(lines_count), str_words]


def wordCount(line,existWords):
    words=line.split(' ')
    l=len(words)
    if len(line)>0 and len(words)==0:
        l=1
        existsWords.append(words)
    else:
        for word in words:
            if(not word in existsWords):
                existsWords.append(word)
    return l



@app.route("/",methods=["GET","POST"])
def index():
    if request.method=='POST':
        file = request.files['file']
        result=count_words_chars_lines(file)
        return render_template("upload.html",notvisibility=1,words=result[0], chars=result[1], lines=result[2], unikWords=result[3])
    return render_template("upload.html", notvisibility=0)

if __name__ == '__main__':
  app.run()

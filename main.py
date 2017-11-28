from flask import Flask, request, render_template, send_from_directory, session, url_for, redirect

app = Flask(__name__)

def count_words_chars_lines(file):
    lines_count=0
    words_count=0
    chars_count=0
    for line in file:
        line=line.decode()
        if(len(line.split('\n'))>1):
            line=line.split('\n')[0]
        else:
            line=line.split('\r\n')[0]
        chars_count+=len(line)
        words_count+=wordCount(line)
        lines_count+=1
    return [str(words_count), str(chars_count), str(lines_count)]


def wordCount(line):
    words=line.split(' ')
    l=len(words)
    if len(line)>0 and len(words)==0:
        l=1
    return l

def get_unique_words_from_file(file):
    words1=[]
    for line in file:
        line=line.decode()
        if(len(line.split('\n'))>1):
            line=line.split('\n')[0]
        else:
            line=line.split('\r\n')[0]
        
        words=line.split(' ')
        if len(line)>0 and len(words)==0 and words not in words1:
            words1.append(words)
            continue
        for word in words:
            if word not in words1:
                words1.append(word)
    return words1

def count_differences(file1,file2):
    distance=0
    similar=0
    words1=get_unique_words_from_file(file1)
    words2=get_unique_words_from_file(file2)
    dist=[]
    for word in words1:
        if word not in words2:
            distance+=1
            dist.append(word)
        else:
            similar+=1
    for word in words2:
        if word not in words1 and word not in dist:
            dist.append(word)
            distance+=1
    return [str(distance), len(words1), len(words2), str(similar)]



@app.route("/")
def index():
        return render_template("index.html")

@app.route("/compare",methods=["GET","POST"])
def compare():
    results_page = "textcounter.azurewebsites.net/compare"
    return render_template("compare.html", notvisibility=0,results_page=results_page)

@app.route("/compare/result",methods=["POST"])
def compare_res():
    if(request.files['file1'].filename!='' and request.files['file2'].filename!=""):
        file1 = request.files['file1']
        file2 = request.files['file2']
        result=count_differences(file1,file2)
        return render_template("compare.html",notvisibility=1,distance=result[0], words1=result[1], words2=result[2], similar=result[3])
    else:
        return redirect(url_for('compare'))

@app.route("/count",methods=["GET","POST"])
def count():
    return render_template("count.html",notvisibility=0)

@app.route("/count/result",methods=["POST"])
def count_res():
    if(request.files['file'].filename!=""):
        print(request.files['file'].filename)
        file = request.files['file']
        result=count_words_chars_lines(file)
        return render_template("count.html",notvisibility=1,words=result[0], chars=result[1], lines=result[2])
    else:
        return redirect(url_for('count'))

if __name__ == '__main__':
  app.run()

from flask import Flask, request, render_template, send_from_directory
import urllib
import numpy as np
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=='POST':
        url='https://www.sciencenews.org/sites/default/files/2016/09/main/articles/090816_ls_brain-training_free.jpg'
        #resp = urllib.urlopen(url)
        #image = np.asarray(bytearray(resp.read()), dtype="uint8")
        #image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return render_template("complete.html")
    return render_template("upload.html")

if __name__ == '__main__':
  app.run(debug=True)

#http://localhost:5000
from flask import Flask, request, render_template, send_from_directory
import os, cv2

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def find_faces(imagePath, s):
	cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

	img = cv2.imread(imagePath)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = cascade.detectMultiScale(
	    gray,
	    scaleFactor=1.1,
	    minNeighbors=5,
	    minSize=(30, 30))#returns a list of rectangles where it believes it found a face

	s[0]=len(faces)

	for (x, y, w, h) in faces:
	    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
	return img

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    
    if not os.path.isdir(target):
            os.mkdir(target)
    #else:
    #    print("Couldn't create upload directory: {}".format(target))

    upload=request.files.getlist("file")[0]
    #filename = upload.filename
    
    destination = "/".join([target, 'temp1.jpg'])
    upload.save(destination)

    size=[0]
    im=find_faces(destination,size)
    cv2.imwrite(destination,im)
    print(size[0])

    return render_template("complete.html", image_name='temp1.jpg', size=size[0])

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == '__main__':
  app.run(port=80)

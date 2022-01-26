from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image

import keras
import numpy as np
from keras.preprocessing import image
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array










app = Flask(__name__)

model = keras.models.load_model("my_model2.h5")

dic1={0:'.ipynb_checkpoints',1:'INCLUDE' ,2:'INTERNALLY   FLAWLESS',3:'SLIGHTLY INCLUDED',4:'VERY SLIGHTLY INCLUDED',5:'VERY_VERY_SLIGHTLY_INCLUDED'}

model.make_predict_function()

def predict(model,img_path):
    test_image = image.load_img(img_path, target_size = (200,200))
    #test_image = image.img_to_array(test_image)
    test_image1 = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image1)
    a=np.argmax(result)
    confidence = round(100 * (np.max(result)), 2)
    return dic1[a],confidence


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "Please subscribe  Artificial Intelligence Hub..!!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		a,b =predict(model,img_path)
		

	return render_template("index.html", prediction = a, img_path = img_path, confidence=b)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)
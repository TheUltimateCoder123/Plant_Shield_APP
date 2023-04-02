from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Define list of class names for your custom dataset
class_names = ['arbus precatorius','madagascar periwinkle','castor oil plant','dieffenbachia','fox glove','lilies','lily of the valley','oleander','pothos','rhubarb','wisteria']

# Load pre-trained EfficientNetV2B3 model
model = tf.keras.models.load_model('model.h5')

# Define a function to preprocess the image before prediction
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(300, 300))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = tf.keras.applications.efficientnet.preprocess_input(x)
    return x

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Load image to predict
    img_file = request.files['image']
    img_path = 'static/uploads/' + img_file.filename
    img_file.save(img_path)
    
    # Preprocess image and make prediction
    x = preprocess_image(img_path)
    preds = model.predict(x)
    class_idx = np.argmax(preds[0])
    class_name = class_names[class_idx]
    
    # Return prediction result
    result = {'class_name': class_name}
    return render_template('result.html', result=result, img_path=img_path)
if __name__ == '__main__':
    app.run(debug=True)

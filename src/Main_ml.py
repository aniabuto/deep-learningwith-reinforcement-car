import time
from io import BytesIO

import keyboard as keyboard

from src.ApiWrapper import Car
import numpy as np
from keras.src.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
from PIL import ImageFile, Image
ImageFile.LOAD_TRUNCATED_IMAGES = True
# Load the model
model = load_model('model_v1.h5')

# Load the weights
model.load_weights('model_weights_v1.h5')

class_names = ['left', 'right', 'straight']


car = Car("192.168.239.249")
car.reset()
car.change_speed()
car.send_data()

start = time.time()
while True:

    t1 = time.time() - start
    if t1 >= 1.5:
        start = time.time()
        response = car.get_picture()

        if response.status_code:
            img = Image.open(BytesIO(response.content))
            image_array = np.array(img)
            predictions = model.predict(np.expand_dims(image_array, axis=0))

            car.steer_direction(class_names[np.argmax(predictions[0])])
            car.send_data()

"""
    No car connected testing:
"""
# image_path = "./2024_01_11_13_04_49.png"
# img = Image.open(image_path)
# resized_image = img.resize((600, 800))
# image_array = np.array(resized_image)
# predictions = model.predict(np.expand_dims(image_array, axis=0))
#
# print(class_names[np.argmax(predictions[0])])

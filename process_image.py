import numpy as np
import cv2
import joblib
from skimage.feature import hog
from skimage import data, exposure

def features_hog(image):
    features = hog(image, orientations=9, pixels_per_cell=(10, 10), cells_per_block=(2, 2), transform_sqrt=True, block_norm="L1")
    return features

def process_image(image):
    test_data = []
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (300, 300))

    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    
    features = features_hog(image)
    test_data.append(features)

    testX = np.array(test_data)

    loaded_model = joblib.load("trained_models/rfc.pkl")
    result = loaded_model.predict(testX)

    return result
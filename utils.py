import cv2
import numpy as np

def preprocess_canvas_image(canvas_image):

    # RGBA -> Gray
    gray = cv2.cvtColor(canvas_image.astype(np.uint8), cv2.COLOR_RGBA2GRAY)

    # Resize directly to MNIST size
    gray = cv2.resize(gray, (28, 28))

    return gray
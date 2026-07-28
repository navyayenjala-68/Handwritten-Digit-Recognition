import numpy as np
import tensorflow as tf

# Load the trained model only once
model = tf.keras.models.load_model("model/digit_model.keras")


def predict_digit(image):
    """
    Predict the handwritten digit from a 28x28 grayscale image.
    """

    # Make sure image matches MNIST format

    image = image.astype("float32") / 255.0
    image = image.reshape(1, 28, 28, 1)

    print("Shape:", image.shape)
    print("Min Pixel:", image.min())
    print("Max Pixel:", image.max())

    prediction = model.predict(image, verbose=0)

    digit = np.argmax(prediction)
    confidence = float(np.max(prediction))

    return digit, confidence, prediction[0]
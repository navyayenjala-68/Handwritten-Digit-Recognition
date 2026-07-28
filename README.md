# ✍️ Handwritten Digit Recognition using CNN

A web-based Handwritten Digit Recognition system built using **TensorFlow**, **Keras**, and **Streamlit**. The model is trained on the **MNIST dataset** and can recognize handwritten digits (0–9) from either a drawing canvas or an uploaded image.

---

## 📌 Project Overview

This project uses a **Convolutional Neural Network (CNN)** to classify handwritten digits. Users can either:

- ✍️ Draw a digit on an interactive canvas
- 📤 Upload an image of a handwritten digit

The application predicts the digit, displays the confidence score, and shows the prediction probabilities for all digits (0–9).

---

## ✨ Features

- 🎨 Draw handwritten digits on a canvas
- 📤 Upload handwritten digit images
- 🤖 CNN-based digit recognition
- 📊 Prediction confidence score
- 📈 Probability chart for all digit classes
- 📌 User-friendly Streamlit interface

---

## 🛠️ Tech Stack

- Python
- TensorFlow
- Keras
- Streamlit
- OpenCV
- NumPy
- Pandas
- Pillow

---

## 🧠 Model Architecture

The CNN model consists of:

- Conv2D (32 filters)
- MaxPooling2D
- Conv2D (64 filters)
- MaxPooling2D
- Flatten
- Dense (128 neurons)
- Dropout
- Dense (10 output classes with Softmax)

---

## 📊 Model Performance

| Metric | Value |
|--------|------:|
| Test Accuracy | **99.24%** |
| Test Loss | **0.0294** |

---

## 📂 Project Structure

```text
Handwritten-Digit-Recognition/
│
├── app.py
├── predict.py
├── utils.py
├── requirements.txt
├── README.md
│
├── model/
│   └── digit_model.keras
│
├── notebooks/
│   └── Handwritten_Digit_Recognition.ipynb
│
├── screenshots/
│
└── images/
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Handwritten-Digit-Recognition.git
```
## 🚀 Live Demo

👉 https://handwritten-digit-recognition-1608200618092.streamlit.app/

Move into the project folder:

```bash
cd Handwritten-Digit-Recognition
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## 💡 Note

For the best prediction accuracy:

- Draw **one digit (0–9)** at a time.
- Keep the digit centered.
- Avoid multiple digits in a single image.
- Upload clear handwritten digit images with minimal background noise.

---

## 🔮 Future Improvements

- Support recognition of multiple handwritten digits.
- Improve preprocessing for uploaded images.
- Deploy the application on Streamlit Community Cloud.
- Add support for custom datasets.

---

## 👨‍💻 Author

**Navya**

Built with ❤️ using TensorFlow and Streamlit.

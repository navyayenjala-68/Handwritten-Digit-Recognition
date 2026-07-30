# ✍️ Handwritten Digit Recognition

An interactive **Deep Learning** web application that recognizes handwritten digits (0–9) using a **Convolutional Neural Network (CNN)** trained on the **MNIST dataset**.

The application allows users to either draw a digit on an interactive canvas or upload an image for prediction. Along with the predicted digit, the system displays the model's confidence score and the probability distribution for all digit classes.

---

# 📌 Project Overview
This project uses a Convolutional Neural Network (CNN) to classify handwritten digits.

The project combines computer vision, image preprocessing, and a CNN model into a user-friendly Streamlit application. It provides real-time predictions while helping users understand the model's confidence through probability visualization.

This project was developed as part of a Machine Learning internship to demonstrate practical Deep Learning deployment using TensorFlow and Streamlit.

---

# ✨ Features

- ✍️ Draw handwritten digits directly on an interactive canvas
- 📤 Upload handwritten digit images
- 🤖 CNN-based digit recognition
- 📊 Real-time prediction
- 📈 Prediction confidence score
- 📉 Probability distribution for all digits (0–9)
- 🎨 Clean and responsive Streamlit interface
- ⚡ Fast prediction using a trained CNN model

---

# 🖼️ Application Preview

## Home Screen

<img width="1522" height="723" alt="Home png" src="https://github.com/user-attachments/assets/f93e70a1-fcc3-43d5-a383-0118a9af5702" />



---

## Draw Digit Prediction


<img width="1512" height="731" alt="draw_prediction png" src="https://github.com/user-attachments/assets/7fb3e03e-d3d0-42aa-87e8-664c3e050b67" />


---

## Upload Image Prediction

<img width="1502" height="682" alt="upload_prediction png" src="https://github.com/user-attachments/assets/e7e4c201-27d6-400d-842e-b362707eda49" />



---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Deep Learning | TensorFlow, Keras |
| Computer Vision | OpenCV |
| Web Framework | Streamlit |
| Image Processing | Pillow |
| Numerical Computing | NumPy |
| Visualization | Matplotlib |
| Dataset | MNIST |

---

# 🧠 Model Architecture

The Convolutional Neural Network consists of the following layers:

```
Input Image (28×28×1)

        │

Conv2D (32 Filters)

        │

MaxPooling2D

        │

Conv2D (64 Filters)

        │

MaxPooling2D

        │

Flatten

        │

Dense (128)

        │

Dropout

        │

Dense (10)

        │

Softmax Output
```

---

# 📊 Model Performance

| Metric | Value |
|--------|------:|
| Dataset | MNIST |
| Test Accuracy | **99.24%** |
| Test Loss | **0.0294** |
| Classes | 10 (Digits 0–9) |

---

# 🔄 Application Workflow

```
User Input
      │
      ▼
Draw Digit / Upload Image
      │
      ▼
Image Preprocessing
      │
      ▼
Resize to 28 × 28
      │
      ▼
Normalize Pixel Values
      │
      ▼
CNN Prediction
      │
      ▼
Predicted Digit
      │
      ▼
Confidence Score
      │
      ▼
Probability Chart
```

---

# 📂 Project Structure

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
│   ├── home.png
│   ├── draw_prediction.png
│   └── upload_prediction.png
│
└── images/
```

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/your-username/Handwritten-Digit-Recognition.git
```

## Navigate to the project

```bash
cd Handwritten-Digit-Recognition
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```
## 🌐 Live Demo

https://handwritten-digit-recognition-1608200618092.streamlit.app/

---

# 💡 Usage

### Draw Mode

- Draw **one handwritten digit (0–9)**.
- Keep the digit centered.
- Avoid multiple digits.
- Click **Predict Drawing**.

### Upload Mode

- Upload a clear handwritten digit image.
- The application automatically preprocesses the image.
- Click **Predict Uploaded Image**.

The application will display:

- Predicted digit
- Confidence percentage
- Probability distribution across all digit classes

---

# 📌 Project Highlights

- CNN trained on the MNIST handwritten digit dataset
- Supports two prediction methods
- Real-time inference
- Interactive probability visualization
- Beginner-friendly Deep Learning project
- Fully deployable using Streamlit

---

# 🔮 Future Improvements

- Multi-digit recognition
- Real-time webcam digit recognition
- Explainable AI using Grad-CAM
- Improved preprocessing for noisy images
- Cloud deployment using Streamlit Community Cloud
- Mobile-friendly responsive interface

---

# ⚠️ Note

For the best prediction accuracy:

- Draw only one digit.
- Keep the digit centered.
- Use thick, clear strokes.
- Upload clean handwritten digit images.
- Avoid noisy backgrounds and multiple digits.

---

# 👨‍💻 Author

**Navya**

Machine Learning • Deep Learning • Computer Vision

Built with ❤️ using **TensorFlow, Keras, OpenCV, and Streamlit**.

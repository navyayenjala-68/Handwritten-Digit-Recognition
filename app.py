import streamlit as st
import pandas as pd
from streamlit_drawable_canvas import st_canvas

from predict import predict_digit
from utils import preprocess_canvas_image

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Handwritten Digit Recognition",
    page_icon="✍️",
    layout="centered"
)

# ---------------- Sidebar ----------------
st.sidebar.title("📌 About")

st.sidebar.markdown("""
### Handwritten Digit Recognition

This project uses a **Convolutional Neural Network (CNN)** trained on the **MNIST dataset**.

### 📊 Model Performance
- Accuracy: **99.24%**
- Loss: **0.0294**

### 🛠 Tech Stack
- TensorFlow
- Keras
- Streamlit
- OpenCV
- NumPy
""")

# ---------------- Title ----------------
st.title("✍️ Handwritten Digit Recognition")

st.info(
    "📝 Draw **one digit (0–9)** in the center of the canvas. "
    "Avoid multiple strokes or multiple digits for the best accuracy."
)
tab1, tab2 = st.tabs(["✍️ Draw Digit", "📤 Upload Image"])

# ---------------- Canvas ----------------
with tab1:

    canvas_result = st_canvas(
        stroke_width=18,
        stroke_color="white",
        background_color="black",
        width=350,
        height=350,
        drawing_mode="freedraw",
        key="canvas",
    )

    st.caption("🗑️ Use the trash icon below the canvas to clear your drawing.")

    if st.button("🔍 Predict Drawing"):

        if canvas_result.image_data is not None:

            image = preprocess_canvas_image(canvas_result.image_data)

            digit, confidence, probabilities = predict_digit(image)

            confidence_percent = confidence * 100

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Predicted Digit", digit)

            with col2:
                st.metric("Confidence", f"{confidence_percent:.2f}%")

            if confidence_percent >= 90:
                st.success("🟢 High Confidence Prediction")
            elif confidence_percent >= 70:
                st.warning("🟡 Moderate Confidence Prediction")
            else:
                st.error("🔴 Low Confidence Prediction")

            chart_df = pd.DataFrame({
                "Digit": list(range(10)),
                "Probability": probabilities
            })

            st.subheader("📊 Prediction Probabilities")
            st.bar_chart(chart_df.set_index("Digit"))

        else:
            st.warning("Please draw a digit first.")

    # Keep the rest of your drawing prediction code here
with tab2:

    from PIL import Image
    import numpy as np

    uploaded_file = st.file_uploader(
        "📤 Upload a handwritten digit",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file).convert("L")

        st.image(image, caption="Uploaded Image", width=200)
        st.info(
    "💡 **Note:** For the best results, upload a clear image containing a **single handwritten digit (0–9)**. "
    "The uploaded image is currently resized to **28×28 pixels** before prediction, so clean, centered images "
    "similar to the MNIST dataset will produce the most accurate results."
)

        if st.button("🔍 Predict Uploaded Image"):

            image = image.resize((28, 28))

            img_array = np.array(image)

            digit, confidence, probabilities = predict_digit(img_array)

            confidence_percent = confidence * 100

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Predicted Digit", digit)

            with col2:
                st.metric("Confidence", f"{confidence_percent:.2f}%")

            if confidence_percent >= 90:
                st.success("🟢 High Confidence Prediction")
            elif confidence_percent >= 70:
                st.warning("🟡 Moderate Confidence Prediction")
            else:
                st.error("🔴 Low Confidence Prediction")

            chart_df = pd.DataFrame({
                "Digit": list(range(10)),
                "Probability": probabilities
            })

            st.subheader("📊 Prediction Probabilities")
            st.bar_chart(chart_df.set_index("Digit"))
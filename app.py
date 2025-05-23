import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="Melanoma Detector", layout="centered")

st.title("🧪 Melanoma Detection (Demo)")
st.markdown("Upload a skin lesion image to get a mock prediction result.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.write("Analyzing...")

    # Mock prediction (replace with real model later)
    fake_result = np.random.choice(["Benign", "Malignant"], p=[0.7, 0.3])
    st.success(f"🧬 Predicted result: **{fake_result}** (Mock Data)")

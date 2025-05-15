# 🧪 Melanoma Detector (Demo)

This is a lightweight Streamlit demo that simulates melanoma classification from skin lesion images.

## 💡 Features
- Upload a skin lesion image (JPG/PNG)
- Simulated prediction result: **Benign** or **Malignant**

## 🚧 Note
This app currently uses **mock results** for demonstration purposes. A real model will be integrated in future versions.

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

---
🔭 **Future Work**
- Integrate a trained CNN model (ResNet34) using ISIC 2018 dataset.
- Add GradCAM heatmap visualization for interpretability.
- Potentially combine patient metadata for multi-modal prediction.
- Inspired by this prototype, I am planning to work on drug response prediction or variant effect modeling in my next project.


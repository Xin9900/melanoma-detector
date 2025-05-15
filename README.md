# 🧪 Melanoma Detector (Demo)

This is a lightweight Streamlit web demo that simulates melanoma classification from skin lesion images.  
It is part of my personal exploration into **AI-assisted diagnostics for early skin cancer detection**.

---

## ✨ Features

- Upload a skin lesion image (JPG/PNG)
- Simulated prediction result: **Benign** or **Malignant**
- Built with: `Python`, `Streamlit`, `Pillow`

---

## 🛠️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

⚠️ Note
This prototype currently uses mock results for demonstration purposes.
A trained deep learning model will be integrated in future versions (ResNet34 on ISIC2018).

🔭 Future Plans
Integrate a real CNN model trained on ISIC 2018 dataset

Add Grad-CAM heatmap for interpretability

Explore multi-modal integration (image + metadata)

Build lightweight web-based health tools for underserved communities

💡 Motivation
This project was inspired by my interest in AI for accessible healthcare.
It represents my early effort to prototype intelligent tools that lower the barrier to early screening.
Based on this, I plan to further explore:

Drug response prediction using multi-omics data

Variant effect modeling for rare genetic diseases

📎 Demo Preview
<img width="777" alt="截屏2025-05-15 下午10 09 00" src="https://github.com/user-attachments/assets/adc5a691-5aff-4fe0-848b-f668e4f4c1a3" />
<img width="836" alt="截屏2025-05-15 下午10 09 17" src="https://github.com/user-attachments/assets/67393e1a-e95b-453b-aea2-01bbe90f98f6" />



👩🏻‍💻 Author
Xinyue(Sherry) Tian · MSc Bioinformatics @ University of Melbourne

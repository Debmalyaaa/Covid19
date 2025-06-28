# 🩺 COVID-19 Chest X-ray Image Classifier using Deep Learning and Streamlit

## 📘 Project Overview

This project is a **deep learning-based web application** that classifies chest X-ray images into three categories:
- **COVID-19**
- **Pneumonia**
- **Normal (Healthy)**

The classifier uses a **Convolutional Neural Network (CNN)** trained on a large publicly available COVID-19 chest X-ray dataset. The web interface is built using **Streamlit**, enabling users to upload an image and receive instant predictions with probability visualizations.

---

## 🎯 Objective

- Detect COVID-19 and other respiratory diseases from chest X-ray images.
- Provide a fast, accessible, and interpretable frontend for clinical or research usage.
- Utilize machine learning and medical datasets to contribute toward public health.

---

## 📂 Dataset Description

The dataset used combines chest X-ray images of:
- **3,616 COVID-19 positive patients**
- **10,192 Normal (healthy) cases**
- **6,012 Lung Opacity (non-COVID infections)**
- **1,345 Viral Pneumonia cases**

### 🔍 Sources

- [RSNA Pneumonia Dataset (Kaggle)](https://www.kaggle.com/c/rsna-pneumonia-detection-challenge/data)
- [Chest X-Ray Pneumonia Dataset (Kaggle)](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)
- [PadChest](https://bimcv.cipf.es/bimcv-projects/bimcv-covid19/)
- [COVID-19 Image Repository](https://github.com/ieee8023/covid-chestxray-dataset)

### 🧾 Citation

If you use this dataset or model in academic research, please cite:
- Chowdhury et al. (2020), *IEEE Access*: “Can AI help in screening Viral and COVID-19 pneumonia?”
- Rahman et al. (2020), *arXiv*: “Exploring the Effect of Image Enhancement Techniques on COVID-19 Detection using Chest X-ray Images.”

---

## 🚀 How It Works

1. **User uploads** a chest X-ray image.
2. The image is **preprocessed** (resized, normalized).
3. A pretrained deep learning model (`covid_classifier.h5`) makes predictions.
4. The **predicted class** and **probabilities** are displayed along with a bar chart.

---

## 🖥️ Web App Features

- Built with **Streamlit**
- Upload `.jpg`, `.jpeg`, or `.png` images
- Displays:
  - Predicted class (COVID, Normal, Pneumonia)
  - Prediction probabilities
  - Bar chart visualization

---

## 🧠 Model Details

- Model Type: **Convolutional Neural Network (CNN)**
- Framework: **TensorFlow / Keras**
- Input shape: **224x224 RGB images**
- Output: 3-class softmax prediction

---

## 🛠️ Tech Stack

| Component        | Technology           |
|------------------|----------------------|
| Frontend         | Streamlit            |
| Model Framework  | TensorFlow / Keras   |
| Image Handling   | PIL, NumPy           |
| Visualization    | Matplotlib           |

---



# 🩺 COVID-19 Chest X-ray Classifier with Deep Learning & Streamlit

## 📘 Project Overview

This project presents a **deep learning-based web application** that detects **COVID-19**, **Pneumonia**, or **Normal** conditions from chest X-ray images. Using a **Convolutional Neural Network (CNN)** trained on medical imaging datasets, the app offers instant predictions through a user-friendly **Streamlit interface**.

The model aims to support radiologists and healthcare practitioners by providing an additional automated tool for rapid and scalable chest image analysis.

---

## 🌍 Motivation

The global COVID-19 pandemic stressed the need for **fast, accurate, and accessible screening methods**. While RT-PCR remains the gold standard, chest X-rays are:

- Widely available
- Cost-effective
- Useful for evaluating lung involvement

This project contributes to ongoing efforts in AI-assisted diagnosis, especially in **low-resource** or **high-volume** settings.

---

## 🎯 Project Goals

- Classify chest X-ray images into:
  - **COVID-19**
  - **Pneumonia**
  - **Normal (Healthy)**
- Provide an interactive, lightweight **web app** for image prediction
- Achieve balance between **accuracy**, **speed**, and **simplicity**

---

## 📂 Dataset Summary

This project leverages a **merged dataset** containing:

| Class         | Image Count |
|---------------|-------------|
| COVID-19      | 3,616       |
| Normal        | 10,192      |
| Pneumonia     | 6,012       |
| Viral Pneumonia (merged) | 1,345  |

> 📦 Data is preprocessed to remove duplicates, resize images to 224x224 pixels, normalize pixel values, and split into training/test sets.

---

## 🧠 Model Architecture

The model is a **CNN** with the following characteristics:

- Input shape: `(224, 224, 3)`
- 3 convolutional blocks with ReLU and max-pooling
- Flattened layers with dropout for regularization
- Dense layers ending with softmax for 3-class classification

### Loss & Optimizer

- Loss Function: `categorical_crossentropy`
- Optimizer: `Adam`
- Evaluation Metric: `accuracy`

---

## 🖥️ Web App Features (Streamlit)

- Upload `.jpg`, `.jpeg`, or `.png` chest X-ray images
- Get real-time predictions: COVID-19, Pneumonia, or Normal
- Probability bar chart visualization
- Clean, responsive UI for clinical/non-clinical users

---

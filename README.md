# 🏠 House Price Prediction Web App

A machine learning-powered web application to predict house prices based on input features like area (in square feet), number of bedrooms, and number of bathrooms. This project is built using **Python**, **Flask**, and **HTML/CSS**, and demonstrates how data science models can be deployed to the web in an interactive and user-friendly way.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Machine Learning Model](#machine-learning-model)
- [Folder Structure](#folder-structure)
- [Setup Instructions](#setup-instructions)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## 📝 Overview

This project uses a **Linear Regression model** trained on dummy housing data (area, bedrooms, bathrooms) to predict the price of a house. The backend is powered by **Flask**, and the frontend uses **HTML/CSS with modern design**.

Users can:
- Enter details of a house
- Click a button to instantly get a price prediction
- See a sleek, modern UI with glassmorphism styling

---

## 🚀 Features

- ✅ Real-time house price prediction
- ✅ Clean, responsive user interface
- ✅ Model training using scikit-learn
- ✅ Web deployment-ready Flask backend
- ✅ Modern glassmorphism and gradient UI

---

## 🧠 Tech Stack

| Layer        | Technology     |
|--------------|----------------|
| Frontend     | HTML5, CSS3 (Glassmorphism styling) |
| Backend      | Python, Flask |
| ML Model     | Linear Regression (scikit-learn) |
| Deployment (Optional) | Render / Replit / Localhost |
| Version Control | Git & GitHub |

---

## 📈 Machine Learning Model

The model is trained using basic tabular data with the following features:

- `area` (int): Area of the house in square feet
- `bedrooms` (int): Number of bedrooms
- `bathrooms` (int): Number of bathrooms

**Model used**: Linear Regression  
**Tool**: scikit-learn  
**Exported file**: `model.pkl`

The `train_model.py` script contains model training and saves the model as a `.pkl` file, which is later used by the Flask app to make predictions.

---
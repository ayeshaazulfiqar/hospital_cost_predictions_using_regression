# 🏥 Hospital Cost Prediction Using Regression Models

## 📌 Project Overview

This project predicts **Annual Medical Cost** using multiple regression techniques.  
The objective is to compare different regression models and evaluate their performance on healthcare insurance data.

The project also includes an interactive interface where users can input patient and insurance details to estimate annual medical costs.

---

## 🎯 Problem Statement

Accurate prediction of medical costs helps:

- Insurance companies assess financial risk
- Patients understand expected healthcare expenses
- Organizations optimize premium pricing strategies

The goal is to predict:

**Dependent Variable (Target):**
annual_medical_cost

Using the following independent features:

**Independent Variables (Features):** 
- monthly_premium
- annual_premium
- total_claims_paid
- avg_claim_amount
- risk_score
- chronic_count

---

## 🛠️ Regression Models Implemented

The following regression models were implemented and compared:

### 1️⃣ Linear Regression
A simple baseline model that assumes a linear relationship between independent variables and the target variable.

### 2️⃣ Ridge Regression
Ridge Regression is a regularized linear regression technique that applies **L2 regularization**.  
It adds a penalty term to the loss function to reduce model complexity and prevent overfitting.

- Helps when features are highly correlated
- Shrinks coefficients but does not eliminate them completely
- Improves generalization performance

### 3️⃣ Lasso Regression
Lasso Regression applies **L1 regularization**, which can shrink some coefficients to zero.  
This makes it useful for automatic feature selection.

### 4️⃣ Elastic Net Regression
Elastic Net combines both **L1 and L2 regularization**, balancing feature selection and coefficient shrinkage.

### 5️⃣ Gradient Boosting Regressor
A powerful ensemble learning method that builds models sequentially and captures non-linear relationships for improved accuracy.


## 📊 Machine Learning Workflow

### 1️⃣ Data Preparation
- Selected relevant features
- Checked data types
- Performed train-test split

### 2️⃣ Feature & Target Definition


y = data['annual_medical_cost']

X = data[['monthly_premium',
          'annual_premium',
          'total_claims_paid',
          'avg_claim_amount',
          'risk_score',
          'chronic_count']]


##  Model Training

Each regression model was trained using the selected independent features to predict the target variable **annual_medical_cost**.

The following models were implemented:

- Linear Regression  
- Lasso Regression  
- Elastic Net Regression  
- Gradient Boosting Regressor  

---

## 4️⃣ Model Evaluation

The models were evaluated using the following performance metrics:

- **R² Score**
- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**

These metrics help measure prediction accuracy and model performance.

---

## 📈 Model Comparison Insights

- **Linear Regression**: Provides a simple baseline model for comparison.  
- **Lasso Regression**: Performs feature selection using L1 regularization.  
- **Elastic Net**: Combines L1 and L2 regularization for better generalization.  
- **Gradient Boosting**: Captures non-linear relationships and often provides improved accuracy.  

> ⭐ Best Model R² Score: *(Add your best R² score here)*

---

## 🖥️ Interactive Prediction Interface

The project includes a simple user interface that allows users to:

- Select a regression model  
- Enter insurance and patient details  
- Adjust risk score and chronic condition count  
- Predict annual medical cost instantly  

## 🔮 Future Improvements

Hyperparameter tuning using GridSearchCV

Cross-validation

Add advanced models (XGBoost, LightGBM)

Deploy using Streamlit or Flask

Add feature importance visualization

## 👩‍💻 Author

### Ayesha Zulfiqar

Machine Learning & Data Science Enthusiast
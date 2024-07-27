# Car Price Prediction Project

## App Link

You can access the deployed application at: [Car Price Prediction App](https://car-price-prediction-4adspnztnhjyglkljp2sr7.streamlit.app/)

## Overview

This project involves predicting the selling price of a car using a Random Forest Regressor model. The model is trained on various car features such as year, present price, kilometers driven, seller type, transmission type, owner, and fuel type. The goal is to estimate the selling price based on these features.

## Key Concepts

### 1. **Feature Engineering and Preprocessing**
   - **Label Encoding**: Used for categorical features such as `Transmission` and `Seller_Type` to convert them into numeric values.
   - **One-Hot Encoding**: Applied to the `Fuel_Type` feature to convert categorical fuel types into binary columns.
   - **Data Transformation**: Ensures that the data fed into the model is in the appropriate format and scale.

### 2. **Model Training and Evaluation**
   - **Random Forest Regressor**: A robust machine learning model used for regression tasks. It works by constructing multiple decision trees and averaging their predictions to improve accuracy and control overfitting.
   - **Performance Metrics**:
     - **Mean Absolute Error (MAE)**: Measures the average magnitude of errors in predictions, representing how far the predicted values are from the actual values.
     - **Mean Squared Error (MSE)**: Measures the average of the squares of errors, giving more weight to larger errors.
     - **R-squared**: Indicates the proportion of variance in the target variable that is predictable from the independent variables, providing a measure of the model’s goodness-of-fit.

### 3. **Model Deployment**
   - **Web Application**: A user-friendly web interface built using Streamlit that allows users to input car details and obtain predictions from the trained model.
   - **Interaction**: Users can enter specific features of the car to get an estimated selling price, making the model accessible for practical use.

## How It Works

1. **Input Features**: Users provide details about the car including year, present price, kilometers driven, seller type, transmission type, owner, and fuel type.
2. **Data Preprocessing**: The app preprocesses these inputs by applying label encoding and one-hot encoding to transform them into a format suitable for the model.
3. **Prediction**: The preprocessed data is then used by the Random Forest model to predict the selling price of the car.
4. **Result**: The app displays the predicted selling price based on the provided inputs.

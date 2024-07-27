import streamlit as st
import pandas as pd
import pickle

# Load the trained model and encoders
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('label_encoder_transmission.pkl', 'rb') as le_trans_file:
    label_encoder_transmission = pickle.load(le_trans_file)

with open('label_encoder_seller_type.pkl', 'rb') as le_seller_file:
    label_encoder_seller_type = pickle.load(le_seller_file)

with open('onehot_encoder_fuel_type.pkl', 'rb') as ohe_file:
    onehot_encoder_fuel_type = pickle.load(ohe_file)

def preprocess_data(data):
    # Apply Label Encoding
    data['Transmission'] = label_encoder_transmission.transform(data['Transmission'])
    data['Seller_Type'] = label_encoder_seller_type.transform(data['Seller_Type'])
    
    # Apply One-Hot Encoding
    fuel_type_encoded = onehot_encoder_fuel_type.transform(data[['Fuel_Type']]).toarray()
    fuel_type_df = pd.DataFrame(fuel_type_encoded, columns=onehot_encoder_fuel_type.get_feature_names_out(['Fuel_Type']))
    data = pd.concat([data, fuel_type_df], axis=1)
    data.drop(['Fuel_Type'], axis=1, inplace=True)
    
    return data

def main():
    st.title('Car Price Prediction')

    # Input fields for features
    year = st.number_input('Year', min_value=1900, max_value=2024, value=2020)
    present_price = st.number_input('Present Price (in lakhs)', min_value=0.0, value=8.5)
    kms_driven = st.number_input('Kms Driven', min_value=0, value=25000)
    seller_type = st.selectbox('Seller Type', ['Dealer', 'Individual'])
    transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
    owner = st.number_input('Owner', min_value=0, value=1)
    fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG'])

    # Prepare the input data
    input_data = pd.DataFrame({
        'Year': [year],
        'Present_Price': [present_price],
        'Kms_Driven': [kms_driven],
        'Seller_Type': [seller_type],
        'Transmission': [transmission],
        'Owner': [owner],
        'Fuel_Type': [fuel_type]
    })

    # Preprocess the data
    input_data = preprocess_data(input_data)

    # Make prediction
    if st.button('Predict Selling Price'):
        prediction = model.predict(input_data)
        st.write(f'Predicted Selling Price: ₹{prediction[0]:.2f} lakhs')

if __name__ == "__main__":
    main()

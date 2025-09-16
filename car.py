import streamlit as st
import pandas as pd

def load_model():
    import joblib   
    model = joblib.load("Packages\car_pred_model.h5")
    return model

st.header("Car Prediction App")
st.subheader("let's predict the selling price...")

with st.form("Car_form"):
    Present_Price = st.number_input("Enter present price of the Car", min_value=0.0, step=1000.0)
    fuel_type = st.selectbox("select Fuel Type", ["Petrol","Diesel", "CNG"])
    seller_type = st.selectbox("select Seller Type",["Dealer", "individual"])
    transmission = st.selectbox("Select Transmission Type", ["Manuel", "Automatic"])

    submit_button = st.form_submit_button("Predict Price")

if submit_button:
    # load the model
    model = load_model()

    # create a DataFrame for the input data
    input_data = {
        "Present_Price": [Present_Price],
        "Fuel_Type": [fuel_type],
        "Seller_Type": [seller_type],
        "Transmission": [transmission]

    }
    data = pd.DataFrame(input_data)

    # Encode categorical variables
    data["Transmission_encoded"] = data["Transmission"].map({"Manual":0, "Automatic":1})
    data["Seller_Type_encoded"] = data["Seller_Type"].map({"Dealer":0, "Individual":1})
    data["Fuel_Type_encodeded"] = data["Fuel_Type"].map({"Petrol":0, "Diesel":1,"CNG":2})
    X= data[["Present_Price","Fuel_Type_encodeded","Seller_Type_encoded","Transmission_encoded"]]

    # predicting
    selling_price = model.predict(X)
    st.write(f"Selling Price: {round(selling_price[0], 2)}")
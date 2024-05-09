import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load the training data
df=pd.read_csv('train_data.csv')

# Define features (X) and response variable (y)
X = df.drop(columns=['target'])
y = df['target']

# Train a RandomForest model
model = RandomForestClassifier(n_estimators=150, max_depth=None, random_state=42)
model.fit(X, y)

# Define feature input function for the app
def user_input_features():
    customer_residence = st.selectbox('Customer Residence Sub County', ['EMBAKASI', 'WESTLANDS', 'DAGORETTI', 'JUJA', 'Other'])
    previously_insured = st.selectbox('Previously Insured', ['No', 'Yes'])
    vehicle_damage = st.selectbox('Vehicle Damage', ['No', 'Yes'])
    annual_premium = st.number_input('Annual Premium', min_value=0, value=10000)
    agent_name = st.selectbox('Agent Name', ['Jomo Kenyatta', 'Obiero Ochieng', 'Gitonga Mwangi', 'Other'])
    customer_age = st.number_input('Customer Age', min_value=18, max_value=100, value=35)
    vehicle_age = st.number_input('Vehicle Age', min_value=0, value=1)

    # Convert categorical variables to binary
    customer_residence_binary = 1 if customer_residence != 'Other' else 0
    previously_insured_binary = 1 if previously_insured == 'Yes' else 0
    vehicle_damage_binary = 1 if vehicle_damage == 'Yes' else 0
    agent_name_binary = 1 if agent_name != 'Other' else 0

    # Create a DataFrame from the user inputs
    data = {
        'Customer_Residence_Sub_County': customer_residence_binary,
        'Previously_Insured': previously_insured_binary,
        'Vehicle_Damage': vehicle_damage_binary,
        'Annual_Premium': annual_premium,
        'Agent_name': agent_name_binary,
        'Customer_Age': customer_age,
        'vehicle_age': vehicle_age
    }

    return pd.DataFrame([data])

# Create the Streamlit app
def main():
    st.title("Customer Interest in Vehicle Insurance Prediction")
    st.write("Fill in the details to predict if the customer is interested in vehicle insurance.")

    user_input_df = user_input_features()

    # Prediction
    if st.button("Predict"):
        prediction = model.predict(user_input_df)[0]
        probability = model.predict_proba(user_input_df)[0][1]  # Probability of being interested
        result = "Interested" if prediction == 1 else "Not Interested"
        st.write(f"Prediction: **{result}** with a probability of **{probability:.2f}**")

if __name__ == '__main__':
    main()
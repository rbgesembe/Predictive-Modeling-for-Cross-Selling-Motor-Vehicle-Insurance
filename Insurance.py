import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the model
with open('modelx.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the list of agent names
agent_names = ['Obiero Ochieng', 'Jomo Kenyatta', 'Wairimu Kariuki', 'Gitonga Mwangi',
               'Onyango Mariga', 'Kimani Mwenda', 'Nyaboke Wamboi', 'Nkatha Nekesa',
               'Wambura Nkatha', 'Mumbi Kinya']

# Create a LabelEncoder object for agent names
label_encoder = LabelEncoder()
label_encoder.fit(agent_names)

# Streamlit UI code
st.title('MV Insurance Cross Sale App')
agent_name = st.selectbox('Agent Name', agent_names)

# Define the minimum and maximum date ranges
min_customer_dob = pd.Timestamp('1930-01-01')
max_customer_dob = pd.Timestamp('2006-01-01')
min_vehicle_yom = pd.Timestamp('2010-01-01')
max_vehicle_yom = pd.Timestamp('2024-01-01')

# Encode the selected agent name
encoded_agent_name = label_encoder.transform([agent_name])[0]

# Define the list of sub counties
sub_counties = ['EMBAKASI','KASARANI','NJIRU','DAGORETTI','THIKA WEST','LUNGA LUNGA','BONDO',
                'KIMININI','TURKANA WEST','KABETE','NAKURU WEST','KAPSERET','TURBO']

# Create a LabelEncoder object for agent names
label_encoder = LabelEncoder()
label_encoder.fit(sub_counties)

# Streamlit UI code
sub_county = st.selectbox('Customer Residence Sub-County', sub_counties)

# Encode the selected agent name
encoded_sub_county = label_encoder.transform([sub_county])[0]

# Input widgets
previously_insured = st.selectbox('Previously Insured', ['Yes', 'No'])
vehicle_damage = st.selectbox('Vehicle Damage', ['Yes', 'No'])
annual_premium = st.slider('Annual Premium', min_value=0.0, max_value=100000.0, step=1000.0)
customer_dob = st.date_input('Customer Date of Birth', min_value=min_customer_dob, max_value=max_customer_dob)
vehicle_yom = st.date_input('Vehicle Year of Manufacture', min_value=min_vehicle_yom, max_value=max_vehicle_yom)

# Initialize StandardScaler for numerical features
scaler = StandardScaler()

# Transform input data
current_year = pd.Timestamp.now().year
annual_premium_scaled = scaler.fit_transform([[annual_premium]])[0][0]
customer_age = (pd.Timestamp.now() - pd.Timestamp(customer_dob)).days // 365
customer_age_scaled = scaler.fit_transform([[customer_age]])[0][0]
vehicle_age = pd.Timestamp.now().year - vehicle_yom.year
vehicle_age_scaled = scaler.fit_transform([[vehicle_age]])[0][0]

# Generate model input data dictionary
input_data = {
    'Agent_name': encoded_agent_name,
    'Previously_Insured': 1 if previously_insured == 'Yes' else 0,
    'Vehicle_Damage':  1 if vehicle_damage == 'Yes' else 0,
    'Annual_Premium': annual_premium_scaled,
    'Customer_Age': customer_age_scaled,
    'vehicle_age_scaled': vehicle_age_scaled,  # Fixed feature name
    'Customer_Residence_Sub_County': encoded_sub_county
}

# Button to trigger prediction
# if st.button('Predict'):
#     prediction = model.predict([list(input_data.values())])
#     st.write('Predicted Response:', prediction[0])

# Button to trigger prediction
# Button to trigger prediction
if st.button('Predict'):
    prediction = model.predict([list(input_data.values())])
    prediction_label = "Interested" if prediction[0] == 1 else "Not interested"
    st.write('Predicted Response:', prediction_label)



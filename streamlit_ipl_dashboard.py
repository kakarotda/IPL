
import streamlit as st
import pandas as pd

# Title of the dashboard
st.title('IPL Team Performance Dashboard')

# Load data
@st.cache
def load_data():
    data = pd.DataFrame({
        'Team': ['Chennai Super Kings', 'Deccan Chargers', 'Delhi Capitals', 'Gujarat Lions', 'Gujarat Titans'],
        'Matches Played': [225, 75, 238, 30, 33],
        'Won': [131, 29, 105, 13, 23],
        'Lost': [91, 46, 127, 16, 10],
        'Draw': [0, 0, 0, 0, 0],
        'Tied': [0, 0, 0, 0, 0]
    })
    return data

# Load the IPL data
ipl_data = load_data()

# Display the dataframe
st.write("IPL Team Data:")
st.dataframe(ipl_data)

# Interactive elements (like a simple filter)
team = st.selectbox('Select a Team:', ipl_data['Team'].unique())
filtered_data = ipl_data[ipl_data['Team'] == team]
st.write(f"Data for {team}:")
st.table(filtered_data)

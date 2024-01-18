
import streamlit as st
import pandas as pd

# Function to load data from the Excel file
@st.cache
def load_data(IPL DATA.xlsx):
    data = pd.read_excel(IPL DATA.xlsx)
    return data

# Function to calculate winning percentage
def calculate_winning_percentage(df):
    df['Winning Percentage'] = (df['Won'] / df['Number of matches played']) * 100
    return df

# Load the IPL data
ipl_data = load_data('IPL DATA.xlsx')

# Calculate winning percentage
ipl_data_with_percentage = calculate_winning_percentage(ipl_data)

# Streamlit app layout
st.title('IPL Team Performance Dashboard')

# Display the dataframe with winning percentage
st.write("IPL Team Data:")
st.dataframe(ipl_data_with_percentage)

# Allow users to select two teams to compare
team1 = st.selectbox('Select Team 1:', ipl_data_with_percentage['Team'].unique())
team2 = st.selectbox('Select Team 2:', ipl_data_with_percentage['Team'].unique())

# Display the comparative analysis
if team1 and team2:
    comparison_data = ipl_data_with_percentage[ipl_data_with_percentage['Team'].isin([team1, team2])]
    st.write('Comparative Analysis:')
    st.dataframe(comparison_data[['Team', 'Number of matches played', 'Won', 'Lost', 'Winning Percentage']])

# Simple prediction based on winning percentage
if st.button('Predict Winner'):
    team1_data = ipl_data_with_percentage[ipl_data_with_percentage['Team'] == team1]
    team2_data = ipl_data_with_percentage[ipl_data_with_percentage['Team'] == team2]
    if not team1_data.empty and not team2_data.empty:
        winner = team1 if team1_data['Winning Percentage'].values[0] > team2_data['Winning Percentage'].values[0] else team2
        st.success(f'The predicted winner is: {winner}')


import streamlit as st
import pandas as pd

# Function to load data (placeholder, replace with actual data loading function)
@st.cache_data
def load_data():
    data = pd.DataFrame({
        'Team': ['Chennai Super Kings', 'Deccan Chargers', 'Delhi Capitals', 'Gujarat Lions', 'Gujarat Titans', 'Kochi Tuskers Kerala', 'Kolkata Knight Riders', 'Lucknow Super Giants', 'Mumbai Indians', 'Pune Warriors', 'Punjab Kings', 'Rajasthan Royals', 'Rising Pune Supergiant', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad'],
        'Matches Played': [225, 75, 238, 30, 33, 14, 237, 30, 247, 46, 232, 206, 30, 241, 166],
        'Won': [131, 29, 105, 13, 23, 6, 119, 17, 138, 12, 104, 101, 15, 114, 78],
        'Lost': [91, 46, 127, 16, 10, 8, 114, 12, 105, 33, 124, 100, 15, 120, 84],
        'Draw': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'Tied': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    })
    return data


# Function to calculate winning percentage
def calculate_winning_percentage(df):
    df['Winning Percentage'] = (df['Won'] / df['Matches Played']) * 100
    return df

# Load the IPL data
ipl_data = load_data()

# Calculate winning percentage
ipl_data_with_percentage = calculate_winning_percentage(ipl_data)

# Streamlit app layout
st.title('IPL Team Performance Dashboard')

# Display the dataframe with winning percentage
st.write("IPL Team Data:")
st.dataframe(ipl_data_with_percentage)

# Bar Chart for Total Wins
st.write("Total Wins by Team:")
st.bar_chart(ipl_data_with_percentage[['Team', 'Won']].set_index('Team'))

# Allow users to select two teams to compare
team1 = st.selectbox('Select Team 1:', ipl_data_with_percentage['Team'].unique())
team2 = st.selectbox('Select Team 2:', ipl_data_with_percentage['Team'].unique())

# Display the comparative analysis
if team1 and team2:
    comparison_data = ipl_data_with_percentage[ipl_data_with_percentage['Team'].isin([team1, team2])]
    st.write('Comparative Analysis:')
    st.dataframe(comparison_data[['Team', 'Matches Played', 'Won', 'Lost', 'Winning Percentage']])

# Simple prediction based on winning percentage
if st.button('Predict Winner'):
    team1_data = ipl_data_with_percentage[ipl_data_with_percentage['Team'] == team1]
    team2_data = ipl_data_with_percentage[ipl_data_with_percentage['Team'] == team2]
    if not team1_data.empty and not team2_data.empty:
        winner = team1 if team1_data['Winning Percentage'].values[0] > team2_data['Winning Percentage'].values[0] else team2
        st.success(f'The predicted winner is: {winner}')



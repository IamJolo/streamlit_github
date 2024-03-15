import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('REMS_Mars_Dataset.csv')

df['earth_date_time'] = pd.to_datetime(df['earth_date_time'].str.split(' ').str[1])
df['sol_number'] = df['sol_number'].str.split(' ').str[1].astype(int)
df['max_ground_temp(°C)'] = df['max_ground_temp(°C)'].replace('Value not available', np.nan).astype(float)
df['min_ground_temp(°C)'] = df['min_ground_temp(°C)'].replace('Value not available', np.nan).astype(float)
df['max_air_temp(°C)'] = df['max_air_temp(°C)'].replace('Value not available', np.nan).astype(float)
df['min_air_temp(°C)'] = df['min_air_temp(°C)'].replace('Value not available', np.nan).astype(float)
df['mean_pressure(Pa)'] = df['mean_pressure(Pa)'].replace('Value not available', np.nan).astype(float)

def generate_air_temp():
    # Select a random row from the dataset
    random_row = df.sample()
    date = random_row['earth_date_time'].iloc[0]
    max_air_temp = random_row['max_air_temp(°C)'].iloc[0]
    return date, max_air_temp


def generate_ground_temp():
    # Select a random row from the dataset
    random_row = df.sample()
    date = random_row['earth_date_time'].iloc[0]
    max_ground_temp = random_row['max_ground_temp(°C)'].iloc[0]
    return date, max_ground_temp

def generate_mean_pressure():
    # Select a random row from the dataset
    random_row = df.sample()
    date = random_row['earth_date_time'].iloc[0]
    mean_pressure = random_row['mean_pressure(Pa)'].iloc[0]
    return date, mean_pressure

# Function to check the user's answer
def check_answer_pressure(mean_pressure, user_answer):
    mean_pressure_high_limit = mean_pressure +10
    mean_pressure_low_limit = mean_pressure - 10
    if user_answer < mean_pressure_high_limit and user_answer > mean_pressure_low_limit:
        return "Richtig, gut gemacht!"
    else:
        return str("Nicht ganz, der maximale Druck war: " + str(mean_pressure) + " Pa")

def check_answer(max_air_temp, user_answer):
    max_air_temp_high_limit = max_air_temp +10
    max_air_temp_low_limit = max_air_temp - 10
    if user_answer < max_air_temp_high_limit and user_answer > max_air_temp_low_limit:
        return "Richtig, gut gemacht!"
    else:
        return str("Nicht ganz, die maximale Temperatur war: " + str(max_air_temp) + " °C")


st.title("Werde zum Mars-Wetterforscher")
image = open("bwl_ien.png", "rb").read()
colx, coly = st.columns([2, 7])
# Display the image in the first column
with colx:
    st.image(image, caption='BWLien', use_column_width=True)
# Display text in the second column
with coly:
    st.write("""Willkommen im Mars-Wetterlabor, kleiner Wissenschaftler! 
    Hier hast du die einmalige Chance, das Wetter auf dem Mars zu analysieren. 
    Betrachte den Graphen, um die Temperatur an verschiedenen Tagen zu bestimmen. 
    Kannst du die Temperatur des Tages erkennen? Trage deine Vermutungen in das Lösungsfeld ein und überprüfe, ob du recht hast. 
    Dieses Spiel macht dich nicht nur zum Experten für das Marswetter, sondern schärft auch dein Verständnis für Daten und Wissenschaft. 
    Mach dich bereit, deine Fähigkeiten als Mars-Wetterforscher unter Beweis zu stellen! """)









st.title("Temperaturen auf dem Mars")
st.write("Bodentemperaturen auf dem Mars")

if 'date' not in st.session_state:
    st.session_state.date = None
if 'max_ground_temp' not in st.session_state:
    st.session_state.max_ground_temp = None
    
if st.button("Open Quiz 1", key= "button1"):
    st.session_state.date, st.session_state.max_ground_temp = generate_air_temp()
    
date = st.session_state.date
max_ground_temp = st.session_state.max_ground_temp

if date is not None and max_ground_temp is not None:
        st.write(f"Wie war die maximale Bodentemperatur(°C) am {date} (+/-10°C) {max_ground_temp} auf dem Mars?")
        user_answer = st.number_input("Enter your answer:", key="input1")
        
        if st.button("Antwort Überprüfen", key= "check1"): 
            result = check_answer(max_ground_temp, user_answer)
            st.write(result)
st.line_chart(df.set_index('earth_date_time')[['max_ground_temp(°C)', 'min_ground_temp(°C)']].dropna())




st.write("Lufttemperaturen auf dem Mars")
if 'date' not in st.session_state:
        st.session_state.date = None
if 'max_air_temp' not in st.session_state:
    st.session_state.max_air_temp = None
    
if st.button("Open Quiz 2", key= "button2"):
    st.session_state.date, st.session_state.max_air_temp = generate_ground_temp()
    
date = st.session_state.date
max_air_temp = st.session_state.max_air_temp

if date is not None and max_air_temp is not None:
        st.write(f"Wie war die Lufttemperatur(°C) am {date} (+/-10°C) {max_air_temp} auf dem Mars?")
        user_answer = st.number_input("Enter your answer:", key="input2")
        
        if st.button("Antwort Überprüfen", key= "check2"): 
            result = check_answer(max_air_temp, user_answer)
            st.write(result)
st.line_chart(df.set_index('earth_date_time')[['max_air_temp(°C)', 'min_air_temp(°C)']].dropna())





st.write("Atmosphärischer Druck auf dem Mars")

if 'date' not in st.session_state:
        st.session_state.date = None
if 'mean_pressure' not in st.session_state:
    st.session_state.mean_pressure = None
    
if st.button("Open Quiz 3", key= "button3"):
    st.session_state.date, st.session_state.mean_pressure = generate_mean_pressure()
    
date = st.session_state.date
mean_pressure = st.session_state.mean_pressure

if date is not None and mean_pressure is not None:
    st.write(f"Wie war der atmosphärischer Druck am {date} (+/-10 Pa) {mean_pressure} auf dem Mars?")
    user_answer = st.number_input("Enter your answer:", key="input3")
        
    if st.button("Antwort Überprüfen", key= "check3"): 
        result = check_answer_pressure(mean_pressure, user_answer)
        st.write(result)
st.line_chart(df.set_index('earth_date_time')['mean_pressure(Pa)'].dropna())




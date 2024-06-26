# Import statements
import streamlit as st
import numpy as np
import pandas as pd

#import dataset
df = pd.read_csv('REMS_Mars_Dataset.csv')

#Citation  I: Diese Seite wurde mit Unterstützung der offiziellen Streamlit-Dokumentation erstellt.
#Citation II: Zusätzlich wurde ChatGPT zur Erklärung der st.session_state Funktion genutzt
#Formatierung der relevanten Spalten ins korrekte Datenformat und richtige Definition der NaN Werte
df['earth_date_time'] = pd.to_datetime(df['earth_date_time'].str.split(' ').str[1])
df['sol_number'] = df['sol_number'].str.split(' ').str[1].astype(int)
df['max_ground_temp(°C)'] = df['max_ground_temp(°C)'].replace('Value not available', np.nan).astype(float)
df['min_ground_temp(°C)'] = df['min_ground_temp(°C)'].replace('Value not available', np.nan).astype(float)
df['max_air_temp(°C)'] = df['max_air_temp(°C)'].replace('Value not available', np.nan).astype(float)
df['min_air_temp(°C)'] = df['min_air_temp(°C)'].replace('Value not available', np.nan).astype(float)
df['mean_pressure(Pa)'] = df['mean_pressure(Pa)'].replace('Value not available', np.nan).astype(float)

#Funktion um zufälligen Lufttemperaturwert aus Datenset zu generieren 
def generate_air_temp():
    random_row = df.sample()
    date = random_row['earth_date_time'].iloc[0]
    max_air_temp = random_row['max_air_temp(°C)'].iloc[0]
    return date, max_air_temp

#Funktion um zufälligen Bodentemperaturwert aus Datenset zu generieren
def generate_ground_temp():
    random_row = df.sample()
    date = random_row['earth_date_time'].iloc[0]
    max_ground_temp = random_row['max_ground_temp(°C)'].iloc[0]
    return date, max_ground_temp

#Funktion um zufälligen Luftdruckwert aus Datenset zu generieren
def generate_mean_pressure():
    random_row = df.sample()
    date = random_row['earth_date_time'].iloc[0]
    mean_pressure = random_row['mean_pressure(Pa)'].iloc[0]
    return date, mean_pressure

# Funktion zur Überpüfung der Antwort für das Luftdruckquiz
def check_answer_pressure(mean_pressure, user_answer):
    mean_pressure_high_limit = mean_pressure +10
    mean_pressure_low_limit = mean_pressure - 10
    if user_answer < mean_pressure_high_limit and user_answer > mean_pressure_low_limit:
        return "Richtig, gut gemacht! Der maximale Druck war: " + str(mean_pressure) + " Pa"
    else:
        return str("Nicht ganz, der maximale Druck war: " + str(mean_pressure) + " Pa")

# Funktion zur Überpüfung der Antwort für beide Temperaturquizze
def check_answer(max_air_temp, user_answer):
    max_air_temp_high_limit = max_air_temp +10
    max_air_temp_low_limit = max_air_temp - 10
    if user_answer < max_air_temp_high_limit and user_answer > max_air_temp_low_limit:
        return "Richtig, gut gemacht! Die maximale Temperatur war: " + str(max_air_temp) + " °C"
    else:
        return str("Nicht ganz, die maximale Temperatur war: " + str(max_air_temp) + " °C")



st.title("Werde zum Mars-Wetterforscher")
image = open("bwl_ien.png", "rb").read()
colx, coly = st.columns([2, 7])

#Anzeige Bild und Text nebeneinander
with colx:
    st.image(image, caption='BWLien', use_column_width=True)

with coly:
    st.write("""Willkommen im Mars-Wetterlabor, kleiner Wissenschaftler! 
    Hier hast du die einmalige Chance, das Wetter auf dem Mars zu analysieren. 
    Betrachte den Graphen, um die Temperatur an verschiedenen Tagen zu bestimmen. 
    Kannst du die Temperatur des Tages erkennen? Trage deine Vermutungen in das Lösungsfeld ein und überprüfe, ob du recht hast. 
    Dieses Spiel macht dich nicht nur zum Experten für das Marswetter, sondern schärft auch dein Verständnis für Daten und Wissenschaft. 
    Mach dich bereit, deine Fähigkeiten als Mars-Wetterforscher unter Beweis zu stellen! """)

# Titel und Beschreibung anzeigen
st.title("Temperaturen auf dem Mars")
st.write("Bodentemperaturen auf dem Mars")

# Überprüfen, ob Datum und maximale Bodentemperatur schon definiert sind, andernfalls auf None setzen
if 'date' not in st.session_state:
    st.session_state.date = None
if 'max_ground_temp' not in st.session_state:
    st.session_state.max_ground_temp = None

# Button zum Öffnen des ersten Quiz und generieren der Zufallswerte    
if st.button("Öffne Quiz 1", key= "button1"):
    st.session_state.date, st.session_state.max_ground_temp = generate_ground_temp()
    
date = st.session_state.date
max_ground_temp = st.session_state.max_ground_temp

# Wenn Datum und maximale Bodentemperatur vorhanden sind wird das Quiz angezeigt 
#(diese Werte werden durch generate_ground_temp() erzeugt, welche aufgerufen werden wenn das Quiz geöffnet wird) 
if date is not None and max_ground_temp is not None:
        st.write(f"Wie war die maximale Bodentemperatur(°C) am {date} (+/-10°C) auf dem Mars?")
        user_answer = st.number_input("Enter your answer:", key="input1")
        
        # Button und Funktionsaufruf zum Überprüfen der Antwort
        if st.button("Antwort Überprüfen", key= "check1"): 
            result = check_answer(max_ground_temp, user_answer)
            st.write(result)
# Linien-Diagramm für die Bodentemperaturen            
st.line_chart(df.set_index('earth_date_time')[['max_ground_temp(°C)', 'min_ground_temp(°C)']].dropna())



# Beschreibung anzeigen
st.write("Lufttemperaturen auf dem Mars")

# Überprüfen, ob Datum und maximale Lufttemperatur schon definiert sind, andernfalls auf None setzen
if 'date' not in st.session_state:
        st.session_state.date = None
if 'max_air_temp' not in st.session_state:
    st.session_state.max_air_temp = None
    
# Button zum Öffnen des zweiten Quiz und generieren der Zufallswerte 
if st.button("Öffnen Quiz 2", key= "button2"):
    st.session_state.date, st.session_state.max_air_temp = generate_air_temp()
    
date = st.session_state.date
max_air_temp = st.session_state.max_air_temp

# Wenn Datum und maximale Lufttemperatur vorhanden sind, das Quiz anzeigen
if date is not None and max_air_temp is not None:
        st.write(f"Wie war die Lufttemperatur(°C) am {date} (+/-10°C) auf dem Mars?")
        user_answer = st.number_input("Enter your answer:", key="input2")
        
        # Button und Funktionsaufruf zum Überprüfen der Antwort
        if st.button("Antwort Überprüfen", key= "check2"): 
            result = check_answer(max_air_temp, user_answer)
            st.write(result)

# Linien-Diagramm für die Lufttemperaturen                       
st.line_chart(df.set_index('earth_date_time')[['max_air_temp(°C)', 'min_air_temp(°C)']].dropna())


# Beschreibung anzeigen
st.write("Atmosphärischer Druck auf dem Mars")

# Überprüfen, ob Datum und Atmosphärendruck schon definiert sind, andernfalls auf None setzen
if 'date' not in st.session_state:
        st.session_state.date = None
if 'mean_pressure' not in st.session_state:
    st.session_state.mean_pressure = None
    
if st.button("Öffne Quiz 3", key= "button3"):
    st.session_state.date, st.session_state.mean_pressure = generate_mean_pressure()
    
date = st.session_state.date
mean_pressure = st.session_state.mean_pressure

# Wenn Datum und Atmosphärendruck vorhanden sind, das Quiz anzeigen
if date is not None and mean_pressure is not None:
    st.write(f"Wie war der atmosphärischer Druck am {date} (+/-10 Pa) auf dem Mars?")
    user_answer = st.number_input("Enter your answer:", key="input3")
        
    # Button und Funktionsaufruf zum Überprüfen der Antwort        
    if st.button("Antwort Überprüfen", key= "check3"): 
        result = check_answer_pressure(mean_pressure, user_answer)
        st.write(result)

# Linien-Diagramm für die Druck                     
st.line_chart(df.set_index('earth_date_time')['mean_pressure(Pa)'].dropna())




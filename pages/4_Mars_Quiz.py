# Import statements
import streamlit as st

import pandas as pd


# Seitenkonfiguration einstellen
st.set_page_config(page_title="Mars Rover Images", page_icon=":computer:")

st.title('Mars Quiz')

image = open("bwl_ien.png", "rb").read()

colx, coly = st.columns([2, 7])
# Anzeige des Bildes in der ersten Spalte
with colx:
    st.image(image, caption='BWLien', use_column_width=True)
# Anzeige des Textes in der zweiten Spalte
with coly:
    st.write("""Willkommen, junger Astronaut! In diesem spannenden Quiz kannst du dein Marswissen testen """)


if 'check_answers' not in st.session_state:
    st.session_state.check_answers = False


if 'correct_answers_count' not in st.session_state:
    st.session_state.correct_answers_count = 0

if 'rerun_trigger' not in st.session_state:
    st.session_state.rerun_trigger = False



#Anzeige der Frage 1
st.subheader("Frage 1: Wie viele Tage hat ein Jahr auf dem Mars?")
# Definition des Radiomenüs mit Antwortmeüs
quiz_answer_1 = st.radio("Wähle die richtige Antwort aus", ["365 Tage", "687 Tage", "55 Tage", "238 Tage"])

#Button um den Antwort auszugeben und Infotext auszugeben
if st.session_state.check_answers:
    infotext_1 = """Ein Marsjahr ist viel länger als ein Jahr auf der Erde! Der Mars benötigt 
                    etwa 687 Tage, um die Sonne einmal zu umkreisen. Das liegt daran, dass seine 
                    Umlaufbahn um die Sonne größer ist als die der Erde."""
    if quiz_answer_1 == "687 Tage":
        st.success("Richtig gemacht!")
        st.write(infotext_1)
        st.session_state.correct_answers_count += 1
        
    else: 
        st.error(" Fast. ")
        st.write(infotext_1)
st.divider()

#Anzeige der Frage 2
st.subheader("Frage 2: Wie hoch ist der höchste Berg auf dem Mars?")
# Definition des Radiomenüs mit Antwortmeüs
quiz_answer_2 = st.radio("Wähle die richtige Antwort aus (Angaben in Kilometern)", [4, 11, 25, 236])

#Button um den Antwort auszugeben und Infotext auszugeben
if st.session_state.check_answers:
    infotext_2 = """Der Olympus Mons auf dem Mars ist der höchste Berg im ganzen Sonnensystem! Er ragt
                    beeindruckende 25 Kilometer über die umliegende Ebene hinaus und ist damit 
                    dreimal so hoch wie der Mount Everest auf der Erde."""
    if quiz_answer_2 == 25:
        st.success(" Richtig gemacht! ")
        st.write(infotext_2)
        st.session_state.correct_answers_count += 1
    else: 
        st.error(" Nicht ganz ")
        st.write(infotext_2)
st.divider()

st.subheader("Frage 3: Welches Element macht den größten Teil der Marsatmosphäre aus?")
quiz_answer_3 = st.radio("Wähle die richtige Antwort aus", ["Sauerstoff", "Stickstoff", "Kohlendioxid", "Wasserstoff"])

if st.session_state.check_answers:
    infotext_3 = """Kohlendioxid (CO2) macht den größten Teil der Marsatmosphäre aus, nämlich etwa 95%. 
    Es gibt nur sehr geringe Mengen anderer Gase wie Stickstoff und Argon. Die geringe Dichte 
    der Atmosphäre und das Fehlen eines starken Magnetfelds führen zu extremen Bedingungen auf der 
    Marsoberfläche, einschließlich extrem niedriger Temperaturen und starker Strahlung.
    """
    if quiz_answer_3 == "Kohlendioxid":
        st.success("Richtig gemacht!")
        st.write(infotext_3)
        st.session_state.correct_answers_count += 1
    else:
        st.error("Leider falsch.")
        st.write(infotext_3)
st.divider()
# Frage 4
st.subheader("Frage 4: Welches Raumschiff landete als erstes erfolgreich auf der Marsoberfläche?")
quiz_answer_4 = st.radio("Wähle die richtige Antwort aus", ["Viking 1", "Mars Pathfinder", "Mars Science Laboratory (Curiosity)", "InSight"])
if st.session_state.check_answers:
    infotext_4 = """Viking 1 landete als erstes erfolgreich auf der Marsoberfläche."""
    if quiz_answer_4 == "Viking 1":
        st.success("Richtig !")
        st.write(infotext_4)
        st.session_state.correct_answers_count += 1
    else:
        st.error("Falsch.")
        st.write(infotext_4)
st.divider()
# Frage 5
st.subheader("Frage 5: Wie wird der Mars auch genannt?")
quiz_answer_5 = st.text_input("Gib deine Antwort ein")

if st.session_state.check_answers:
    correct_answer_5 = ["der rote planet", "rote", "roter planet", "rote planet"]
    infotext_5 = """Der Mars wird oft als "Der rote Planet" bezeichnet aufgrund seiner charakteristischen roten Färbung."""
    if quiz_answer_5.lower() in correct_answer_5:
        st.success("Richtig!")
        st.write(infotext_5)
        st.session_state.correct_answers_count += 1
    else:
        st.error("Falsch.")
        st.write(infotext_5)

st.divider()

# Frage 6
st.subheader("Frage 6: Wie viele Monde hat der Mars?")
quiz_answer_6_options = ["1", "2", "6", "13"]
quiz_answer_6 = st.selectbox("Wähle die richtige Antwort aus", quiz_answer_6_options)

if st.session_state.check_answers:
    correct_answer_6 = "2"
    infotext_6 = """Der Mars hat zwei Monde namens Phobos und Deimos."""
    if quiz_answer_6 == correct_answer_6:
        st.success("Richtig!")
        st.write(infotext_6)
        st.session_state.correct_answers_count += 1
    else:
        st.error("Falsch.")
        st.write(infotext_6)
st.divider()

# Frage 7
st.subheader("Frage 7: Wie lange dauert es, eine Nachricht von der Erde zum Mars zu senden?")
quiz_answer_7 = st.radio("Wähle die richtige Antwort aus", ["etwa 3 Minuten", "etwa 8 Minuten", "etwa 12 Minuten", "etwa 20 Minuten"])
if st.session_state.check_answers:
    infotext_7 = """Es dauert etwa 8 Minuten, eine Nachricht von der Erde zum Mars zu senden. Die genaue Zeit hängt von 
    der relativen Position der beiden Planeten in ihren Umlaufbahnen um die Sonne ab."""
    if quiz_answer_7 == "etwa 8 Minuten":
        st.success("Richtig gemacht!")
        st.write(infotext_7)
        st.session_state.correct_answers_count += 1
    else:
        st.error("Falsch.")
        st.write(infotext_7)
st.divider()

# Frage 8
st.subheader("Frage 8: Welcher Mars-Rover entdeckte erstmals Wasser auf dem Mars?")
quiz_answer_8 = st.radio("Wähle die richtige Antwort aus", ["Opportunity", "Curiosity", "Perseverance", "Spirit"])
if st.session_state.check_answers:
    infotext_8 = """Der Mars-Rover Curiosity entdeckte erstmals  Wasser auf dem Mars. Die Analyse von 
    Gesteinsproben zeigte Anzeichen für früheres flüssiges Wasser auf der Marsoberfläche."""
    if quiz_answer_8 == "Curiosity":
        st.success("Richtig gemacht!")
        st.write(infotext_8)
        st.session_state.correct_answers_count += 1
    else:
        st.error("Fast, aber nicht ganz.")
        st.write(infotext_8)
st.divider()

#Frage 9
st.subheader("Frage 9: Welches Jahr markierte den Beginn der ersten erfolgreichen Marsmission?")
quiz_answer_9 = st.radio("Wähle die richtige Antwort aus", ["1965", "1971", "1997", "2004"])
if st.session_state.check_answers:
    infotext_9 = """Das Jahr 1971 markierte den Beginn der ersten erfolgreichen Marsmission mit der Ankunft der sowjetischen Sonde Mars 3."""
    if quiz_answer_9 == "1971":
        st.success("Korrekt!")
        st.write(infotext_9)
        st.session_state.correct_answers_count += 1
    else:
        st.error("Leider falsch.")
        st.write(infotext_9)
st.divider()

#Frage 10
st.subheader("Frage 10: Wie viele erfolgreiche Landungen auf dem Mars wurden bisher durchgeführt?")
quiz_answer_10 = st.radio("Wähle die richtige Antwort aus", ["3", "7", "13", "21"])
if st.session_state.check_answers:
    infotext_10 = """Bisher wurden insgesamt 7 erfolgreiche Landungen auf dem Mars durchgeführt."""
    if quiz_answer_10 == "7":
        st.success("Richtig!")
        st.write(infotext_10)
        st.session_state.correct_answers_count += 1
    else:
        st.error("Fast, aber nicht ganz.")
        st.write(infotext_10)
st.divider()

check_button = st.button("Antwort prüfen", key="quizbutton1")

if check_button:
    st.session_state.check_answers = True
    st.rerun()

# Check answers if the button is pressed
if st.session_state.check_answers:
    
    # Display results immediately after answer checking
    chart_data = pd.DataFrame({
        "Antworten": ["Richtig", "Falsch"],
        "Anzahl": [st.session_state.correct_answers_count, 10 - st.session_state.correct_answers_count],
    })

    # Display bar chart
    st.subheader("Dies sind deine Resultate")
    st.bar_chart(chart_data.set_index("Antworten"))
    st.session_state.rerun_trigger = True



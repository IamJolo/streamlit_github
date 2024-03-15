

# Import statements
import streamlit as st
import pandas as pd
from PIL import Image
import requests
from io import BytesIO

# Set page config
st.set_page_config(page_title="Mars Rover Images", page_icon=":computer:")


st.title('Mars Entdecker')

image = open("bwl_ien.png", "rb").read()
colx, coly = st.columns([2, 7])
# Display the image in the first column
with colx:
    st.image(image, caption='BWLien', use_column_width=True)
# Display text in the second column
with coly:
    st.write("""Willkommen, junger Astronaut! Ich bin das BWL-Lien, dein Guide auf dieser faszinierenden Reise durch das Weltall. 
    Bist du bereit, die Geheimnisse des roten Planeten zu entdecken? Bei MarsEntdecker erwarten dich spannende Abenteuer und Spiele, die dein Wissen über den Mars erweitern. """)


# Adding widgets to the main area
st.title('Entdecke Mars-Aufnahmen')
st.write("""Hallo, Weltraumforscher! Klick dich durch atemberaubende Aufnahmen des Mars und erfahre 
mehr über seine geheimnisvolle Oberfläche. Jedes Bild erzählt eine Geschichte aus einer fernen Welt. 
Entdecke Krater, Staubstürme und vielleicht sogar Hinweise auf Wasser! Mit jedem Bild, das du erkundest, 
kommst du dem Mars ein Stück näher. Bist du bereit, in die Fußstapfen eines echten Marsforschers zu treten?.

Gib einfach ein Datum ein und clicke auf "Ergebnisse anzeigen"
""")



    
col3, col2, col1 = st.columns(3)
with col1:
    year = st.number_input("Jahr", min_value=2004, max_value=2018, step=1, value = 2009)
with col2:
    month = st.number_input("Monat", min_value=1, max_value=12, step=1, value= 3)
with col3:
    day = st.number_input("Tag", min_value=1, max_value=31, step=1, value=1)

loop_interval = st.number_input("Anzahl ausgegebener Bilder", min_value=1, step=1, value= 15)


remaining_api_calls = 40
# Function to display image from URL
def display_image_from_url(url,description):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    st.image(image, caption=description, use_column_width=True)

if st.button("Ergebnisse anzeigen"):
    # Call the NASA picture API
    api_start = "https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/photos?earth_date="
    api_date = str(year)+"-"+str(month)+"-"+str(day)
    api_date_rest = "&api_key="
    api_key = "DEMO_KEY"
    api_url = api_start + api_date + api_date_rest + api_key
    print(api_url)
    response = requests.get(api_url)
    complete_json = response.json()
    picture_urls = []
    camera_description =[]
    remaining_api_calls = response.headers["X-Ratelimit-Remaining"]
    if len(complete_json["photos"]) == 0:
        st.write("Für dieses Datum sind keine Daten verfügbar. Versuchen Sie einen anderen!")
    
    for i in range(len(complete_json["photos"])):
        picture_urls.append(complete_json["photos"][i]['img_src'])
        camera_description.append(complete_json["photos"][i]["camera"]["full_name"])


    # Streamlit UI
    st.title('NASA Opportunity Rover Mars Bilder')

    # Display images in two columns
    col1, col2 = st.columns(2)
    
    
    for i, url in enumerate(picture_urls):
        with (col1 if i % 2 == 0 else col2):
            description = "Opportunity Rover Bild: " + str(i+1) + " Kamera: " + camera_description[i]
            if '.jpl' in url:
                url = url.replace('.jpl', '')
            display_image_from_url(url, description)
            
        if (i+1) % loop_interval ==0:
            break
    st.write("Du hast: " + str(remaining_api_calls) + " Aufrufe übrig (API calls).")




# Import statements
import streamlit as st
import pandas as pd
from PIL import Image
import requests
from io import BytesIO

# Seitenkonfiguration einstellen
st.set_page_config(page_title="Mars Rover Images", page_icon=":computer:")

st.title('Mars Quiz')

image = open("bwl_ien.png", "rb").read()
import streamlit as st
import google.generativeai as genai
import os

st.title("Mon Assistant IA")

# On récupère la clé secrète (on la configurera à l'étape 4)
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# Champ pour poser la question
user_input = st.text_input("Pose ta question ici :")

if user_input:
    # On appelle le modèle (Gemini)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_input)

    # On affiche la réponse
    st.write(response.text)

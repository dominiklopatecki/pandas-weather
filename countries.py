import requests
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dane",layout ="wide")
st.title("Kraje świata - Przewodnik")


def get_countries(fields):
    plain = ','.join(fields)
    URL = f"https://restcountries.com/v3.1/all?fields={plain}"
    try:
        response = requests.get(URL)
        data = response.json()
        #print(data)
        countries = []
        for country in data:
            countries.append({
                "nazwa":country["name"]["common"],
                "oficjalna_nazwa":country["name"]["official"],
                "stolica": country.get("capital","Brak"),
                "populacja":country.get("population",0),
                #flaga - link do flagi
                #godlo - link do godła
                #kontynent - lista kontynentów
                "flaga": country.get("flags").get("png"),
                "godlo": country.get("coatOfArms").get("png"),
                "kontynent":country.get("continents")[0]

            })
        return countries
    except Exception as err:
        print("wystąpił błąd",err)

countries = get_countries(["name","population","flags","coatOfArms","continents"])


df = pd.DataFrame (countries)

continent = st.sidebar.multiselect(
    "continent",
    options=df["kontynent"].unique()
)

st.dataframe(df,key="continent")
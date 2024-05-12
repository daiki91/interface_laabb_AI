from datetime import time
import hydralit as hy
import streamlit as st
import hydralit_components as hc
from urllib.error import URLError
import pandas as pd
import altair as alt
import numpy as np
import folium
from streamlit_folium import folium_static
from urllib.error import URLError
from accueil import Accueil
# from presentation.sql import get_db_connections

# from sidebar.sidebar import get_selected_model


app = hy.HydraApp(title='Secure Hydralit Data Explorer',
                  favicon="🚀",hide_streamlit_markers=True,
                  use_navbar=True, navbar_sticky=True,
                #   banner_spacing=[30,20,40,30,10]
                  )

@app.addapp()
def home():
    # image lambtech
    # st.image('./iibs.png')
    # Définition du style CSS pour les cartes
    st.markdown(
        """
        <style>
        .card {
            padding: 20px 20px 20px 70px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            background-color: #F4EFEF;
            transition: box-shadow 0.3s ease;
        }
        .card:hover {
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    with col1:
    # Define the card content as HTML string
        ml_description = "Description ou contenu lié au Machine Learning."
        card_content = f"""
        <div class="card">
            <h3>Machine Learning</h3>
            <p>{ml_description}</p>
        </div>
        """
        st.markdown(card_content, unsafe_allow_html=True)
    with col2:
    # Define the card content as HTML string
        ml_description = "communiquer avec les humains et d'autres systèmes, généralement via un langage naturel ou des interfaces utilisateur. ."
        card_content = f"""
        <div class="card">
            <h3>Machine Learning"Communication"</h3>
            <p>{ml_description}</p>
        </div>
        """
        st.markdown(card_content, unsafe_allow_html=True)

        br_content = f"""
        <div >
            <br>
        </div>
        """
        st.markdown(br_content, unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        ml_description = "percevoir leur environnement grâce à des capteurs, des caméras, des microphones, etc., leur permettant de comprendre et d'interagir avec le monde réel."
        card_content = f"""
        <div class="card">
            <h3>Machine Learning"Perception"</h3>
            <p>{ml_description}</p>
        </div>
        """
        st.markdown(card_content, unsafe_allow_html=True)
    with col4:
    # Define the card content as HTML string
        ml_description = "Description ou contenu lié au Machine Learning."
        card_content = f"""
        <div class="card">
            <h3>Machine Learning</h3>
            <p>{ml_description}</p>
        </div>
        """
        st.markdown(card_content, unsafe_allow_html=True)
    
 

@app.addapp(title='Accueil')
# @app.addapp(title='AI_n_BD', icon="🥰")
def model1():
     Accueil()
    #  hy.info("Bienvenue sur la page d'accueil présentée par les étudiants de l'esp groupe 8 à l'occasion du panel Lamb Tech")


@app.addapp(title='formulaire')
def model2():
    hy.info('Hello form formulaire')# st.write(nom_list)
    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")
        annee_naissance = st.slider("anne de naissance : ",1960,2024,2005)
        numero_tel = st.number_input("Numéro de téléphone")
        print(770000000 <= numero_tel and  numero_tel<= 779999999)
                

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)
            st.write(annee_naissance)


# #Le sidebar 
# selected_model = get_selected_model()
# if selected_model == "Accueil":
#     Accueil()
# elif selected_model == "model2":
#     model2()
# else:
#   # Display default content if no model is selected
#   st.write("Please select a model from the sidebar.")


# Page dataset avec graphiques interactifs
@app.addapp(title='dataset')
def model6():
    st.title("dataset")

    try:
        # Charger le fichier CSV à partir de l'emplacement local ou d'une URL
        # Assurez-vous que le fichier iibs_dataM1.csv est dans le même répertoire que votre script Python
        df = pd.read_csv('iibs_dataM1.csv').set_index(["Area", "Item", "Year"])

        # Convertir les colonnes nécessaires en numériques si elles ne le sont pas déjà
        numeric_columns = ["hg/ha_yield", "average_rain_fall_mm_per_year", "pesticides_tonnes", "avg_temp"]
        df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")

        # Nettoyer les données en remplaçant les valeurs non numériques par NaN
        df_cleaned = df.apply(pd.to_numeric, errors="coerce")

        # Sélection des régions à afficher
        countries = st.multiselect(
            "Sélectionnez des Régions", df_cleaned.index.levels[0], []
        )
        if not countries:
            st.error("Veuillez sélectionner au moins une région.")
        else:
            data = df_cleaned.loc[countries] / 1000000.0
            st.write("### Production agricole brute ($B)", data.sort_index())

            # Création de la carte du Sénégal avec les différentes régions
            senegal_map = folium.Map(location=[14.4974, -14.4524], zoom_start=7)
            regions_layer = folium.FeatureGroup(name='Regions')

            for region in countries:
                region_data = df_cleaned.loc[region]
                region_popup = f"{region}: {region_data['hg/ha_yield']} hg/ha_yield"
                folium.Marker(
                    location=[14.4974, -14.4524],
                    popup=region_popup,
                    icon=folium.Icon(color='blue', icon='info-sign')
                ).add_to(regions_layer)

            senegal_map.add_child(regions_layer)
            senegal_map.add_child(folium.LayerControl())
            folium_static(senegal_map)

            data = data.reset_index().melt(id_vars=["Year"], value_vars=numeric_columns).rename(
                columns={"Year": "année", "value": "Production agricole brute ($B)"}
            )
            chart = (
                alt.Chart(data)
                .mark_area(opacity=0.3)
                .encode(
                    x="année:T",
                    y=alt.Y("Production agricole brute ($B):Q", stack=None),
                    color="Area:N",
                )
            )
            st.altair_chart(chart, use_container_width=True)
    except URLError as e:
        st.error(f"Erreur de connexion : {e.reason}")
# Charger les données à partir du fichier CSV
# df = pd.read_csv('iibs_dataM1.csv')

# # Page dataset avec graphiques interactifs
# @app.addapp(title='dataset')
# def model6():
#     st.title("dataset")

#     # Afficher le DataFrame dans l'application Streamlit
#     st.write(df)

#     # Graphique interactif avec Plotly
#     fig = px.line(df, x='Year', y='hg/ha_yield', color='Area', title='Yield by Year and Area')
#     st.plotly_chart(fig)

        # ////////////////////////////////////////////////////////////
# Page dataframe avec graphiques interactifs
@app.addapp(title='dataframe')
def model3():
    st.title("dataframe")
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    try:
        df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz").set_index("Region")
        countries = st.multiselect(
            "Sélectionnez des pays", list(df.index), ["thies", "Matam"]
        )
        if not countries:
            st.error("Veuillez sélectionner au moins un pays.")
        else:
            data = df.loc[countries] / 1000000.0
            st.write("### Production agricole brute ($B)", data.sort_index())

            data = data.T.reset_index()
            data = pd.melt(data, id_vars=["index"]).rename(
                columns={"index": "année", "value": "Production agricole brute ($B)"}
            )
            chart = (
                alt.Chart(data)
                .mark_area(opacity=0.3)
                .encode(
                    x="année:T",
                    y=alt.Y("Production agricole brute ($B):Q", stack=None),
                    color="Region:N",
                )
            )
            st.altair_chart(chart, use_container_width=True)
    except URLError as e:
        st.error(f"Erreur de connexion : {e.reason}")
# Page graphe avec graphiques interactifs
@app.addapp(title='graphe')
def model4():
    st.title("graphe")
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


# Page modele 5 avec graphiques interactifs
@app.addapp(title='modele 5')
def model5():
    st.title("modele 5")
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")

app.run()

import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

import hydralit as hy

app = hy.HydraApp(
    title='Secure Hydralit Data Explorer',
    favicon="🚀",
    hide_streamlit_markers=True,
    use_navbar=True,
    navbar_sticky=True
)

# Fonction pour créer une carte HTML
def create_card(title, description):
    return f"""
    <div class="card">
        <h3>{title}</h3>
        <p>{description}</p>
    </div>
    """

# Page d'accueil avec des cartes
@app.addapp()
def home():
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

    st.title("Accueil")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(create_card("Machine Learning 1", "Description ou contenu lié au Machine Learning."))
    with col2:
        st.markdown(create_card("Machine Learning 2", "Description ou contenu lié au Machine Learning."))

# Page modèle 2 avec formulaire interactif
@app.addapp(title='Modèle 2')
def model2():
    st.title("Modèle 2")
    with st.form("my_form"):
        st.write("À l'intérieur du formulaire")
        slider_val = st.slider("Curseur du formulaire")
        checkbox_val = st.checkbox("Case à cocher du formulaire")
        annee_naissance = st.slider("Année de naissance :", 1960, 2024)
        numero_tel = st.number_input("Numéro de téléphone")
        
        if 770000000 <= numero_tel <= 779999999:
            st.write("Le numéro de téléphone est valide.")
        else:
            st.warning("Le numéro de téléphone n'est pas valide.")

        submitted = st.form_submit_button("Envoyer")
        if submitted:
            st.write("Curseur :", slider_val, "Case à cocher :", checkbox_val)
            st.write("Année de naissance :", annee_naissance)

# Page modèle 3 avec graphiques interactifs
@app.addapp(title='Modèle 3')
def model3():
    st.title("Modèle 3")
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    try:
        df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz").set_index("Region")
        countries = st.multiselect(
            "Sélectionnez des pays", list(df.index), ["China", "United States of America"]
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

app.run()

import streamlit as st
import hydralit as hy
import numpy as np
from joblib import load
from assistant import main
from assistant import risque

# def formulaire():
     

dtr = load('dtr.hdf5')
preprocesser= load('preprocesser.hdf5')
def prediction(Year, types_de_sols,average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item):
    # Create an array of the input features
    features = np.array([[Year,types_de_sols ,average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item]], dtype=object)

    # Transform the features using the preprocessor
    transformed_features = preprocesser.transform(features)

    # Make the prediction
    predicted_yield = dtr.predict(transformed_features).reshape(1, -1)

    return predicted_yield[0]

def Accueil():
    
    st.sidebar.header("Bienvenue sur **AGRIFARM**")
    def show_model1():
        # st.write("Contenu Tableau de Bord")
        st.subheader("Bienvenue sur **AGRIFARM**, la plateforme qui vous accompagne dans la gestion de votre exploitation agricole.")
        st.markdown("""***Vous trouverez ici des outils pour vous aider à prendre des décisions éclairées.***""")

        # Add buttons for key performance indicators
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("Rendement", key="rendement"):
                st.write(f"<div style='padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); background-color: #f0f0f0;'><h3>Rendement:  kg/ha</h3></div>", unsafe_allow_html=True)
        
        with col2:
            if st.button("Coûts", key="couts"):
                st.write("<div style='padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); background-color: #f0f0f0;'><h3>Coûts: $5000</h3></div>", unsafe_allow_html=True)
        
        with col3:
            if st.button("Bénéfices", key="benefices"):
                st.write("<div style='padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); background-color: #f0f0f0;'><h3>Bénéfices: $10000</h3></div>", unsafe_allow_html=True)
        
        with col4:
            if st.button("Générer un rapport détaillé", key="rapport"):
                st.write("<div style='padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); background-color: #f0f0f0;'><h3>Rapport détaillé généré!</h3></div>", unsafe_allow_html=True)
    def show_model_2():
        st.subheader("Renseigner les informations")
        with st.form(key = 'infos_pluie'):
            annee = st.slider("Annee", 1990, 2030, 2023 )
            type_sol = st.selectbox("Type de sol", ["Argileux", "Sableux", "Limoneux"])
            type_culture = st.selectbox("Type de culture", ['Mais', 'Pattate', 'Rice', 'Sorgho', 'Mil', 'Arachide', 'Fonio','Manioc', 'Niebe', 'Bissap'])
            precip_moy_an = st.number_input("Précipitations moyennes en millimètres par an")
            pesti_tonne = st.number_input("Pesticides en tonnes")
            temp_moy = st.text_input("Temperature moyenne")
            Region = st.text_input("La region")

            submitted = st.form_submit_button()
            if submitted:  
                form_data = {
                    "annee": annee,
                    "type_sol": type_sol,
                    "type_culture": type_culture,
                    "precip_moy_an": precip_moy_an,
                    "pesti_tonne": pesti_tonne,
                    "temp_moy": temp_moy,
                    "Region": Region
                }
                st.success("formulaire soumis avec succes!")
                "Year	types_de_sols	average_rain_fall_mm_per_year	pesticides_tonnes	avg_temp	Area	Item"
                prediction_yield = prediction(form_data["annee"], form_data["type_sol"], form_data["precip_moy_an"], form_data["pesti_tonne"], form_data["temp_moy"], form_data["Region"], form_data["type_culture"])
                st.write(f"le rendement prevue est de {prediction_yield [0]} quintaux ou (10^2 Kg)/hectare")
                return prediction_yield[0]
    def show_model_3():
            cout = st.number_input("Coût de production (À combien estimez-vous le coût de production total?)")
            culture_cout = st.number_input("Quel est le prix du marché de la culture? (Prix de vente de la culture)")
            if st.button("Estimer les coûts et les revenus"):
                revenu = show_model_2() * culture_cout
                benefice = revenu - cout
                st.subheader(f"Le revenu estimé est de :  {revenu} FCFA")

    def show_model_4():
            # st.write("Contenu du Recommandations")
            main()

    def show_model_5():
            # st.write("Risques Climatiques et Agricoles")
            risque()
                


    selected_model = st.sidebar.radio("", ["Tableau de Bord","Analyse et Prévision", "Estimation des Coûts et Revenus", "Recommandations", "Risques Climatiques et Agricoles"])

    if selected_model == "Tableau de Bord":
        show_model1()
    elif selected_model == "Analyse et Prévision":
        show_model_2()
    elif selected_model == "Estimation des Coûts et Revenus":
        show_model_3()
    elif selected_model == "Recommandations":
        show_model_4()
    elif selected_model == "Risques Climatiques et Agricoles":
        show_model_5()


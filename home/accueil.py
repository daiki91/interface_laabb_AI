import streamlit as st
import hydralit as hy

def Accueil():
    st.sidebar.header("Bienvenue sur AGRIFARM")
    def show_model1():
        st.write("Contenu du Modèle 1")
    def show_model_2():
        st.subheader("Renseigner les informations")
        with st.form(key = 'infos_pluie'):
            annee = st.slider("Annee", 1990, 2030, 2023 )
            type_sol = st.selectbox("Type de sol", ["Argileux", "Sableux", "Limoneux"])
            type_culture = st.selectbox("Type de culture", ["Céréales", "Légumes", "Fruits"])
            prenom = st.text_input("Précipitations moyennes en millimètres par an")
            pet = st.text_input("Pesticides en tonnes")
            temp_moy = st.text_input("Temperature moyenne")

            submitted = st.form_submit_button()
            if submitted:  
                form_data = {
                    "annee": annee,
                    "type_sol": type_sol,
                    "type_culture": type_culture,
                    "prenom": prenom,
                    "pet": pet,
                    "temp_moy": temp_moy
                }
                st.success("formulaire soumis avec succes!")
                st.write(form_data)
    def show_model_3():
            st.write("Contenu du Modèle 3")
    def show_model_4():
            st.write("Contenu du Modèle 4")
    selected_model = st.sidebar.radio("", ["Tableau de Bord","Analyse et Prévision", "Estimation des Coûts et Revenus", "Recommandations ", "Risques Climatiques et Agricoles"])

    if selected_model == "Tableau de Bord":
        show_model1()
    elif selected_model == "Analyse et Prévision":
        show_model_2()
    elif selected_model == "Estimation des Coûts et Revenus":
        show_model_3()
    elif selected_model == "Risques Climatiques et Agricoles":
        show_model_4()


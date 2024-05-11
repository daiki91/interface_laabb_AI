import streamlit as st
import hydralit as hy

def Accueil():
    st.sidebar.header("Bienvenue sur AGRIFARM")
    def show_model1():
        st.write("Contenu du Modèle 1")
    def show_model_2():
        st.write("Contenu du Modèle 2")
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


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
            precip_moy_an = st.number_input("Précipitations moyennes en millimètres par an")
            pesti_tonne = st.number_input("Pesticides en tonnes")
            temp_moy = st.text_input("Temperature moyenne")

            submitted = st.form_submit_button()
            if submitted:  
                form_data = {
                    "annee": annee,
                    "type_sol": type_sol,
                    "type_culture": type_culture,
                    "precip_moy_an": precip_moy_an,
                    "pesti_tonne": pesti_tonne,
                    "temp_moy": temp_moy
                }
                st.success("formulaire soumis avec succes!")
                st.write(form_data)
    def show_model_3():
        st.write("Contenu du Modèle 3")
    def show_model_4():
        st.header("Posez vos questions ici")
        # st.write("Quel est le risque climatique le plus fréquent?")
        # st.write("Que faire en cas de sécheresse?")
        # st.write("Comment prévenir les maladies des plantes?")
        # st.write("Comment prévenir les attaques des ravageurs?")
       
        st.markdown("""***Quel est le risque climatique le plus fréquent?***""")
        st.markdown("""***Que faire en cas de sécheresse?***""")
        st.markdown("""***Comment prévenir les maladies des plantes?***""")
        st.markdown("""***Comment prévenir les attaques des ravageurs?***""")
            
    def show_model_5():
        st.write("Contenu du Modèle 5")
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


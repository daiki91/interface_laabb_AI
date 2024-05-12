import streamlit as st
from sql import get_db_connection
# from home.home import home

def presentation():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    if db_connection.is_connected():
        print("Connected to MySQL database")

    menu = ["Inscription", "Connection"]
    choice = st.sidebar.selectbox("Menu", menu)
    choice =="Connection"

    if choice == "Inscription":
        st.title("Page Inscription")
        # Logique du formulaire d'inscription
        with st.form(key='inscription_form'):
            st.subheader("Formulaire d'Inscription")
            nom = st.text_input("Nom")
            prenom = st.text_input("Prénom")
            email = st.text_input("Email (sans le @gmail.com)") + "@gmail.com"
            mot_de_passe = st.text_input("Mot de passe", type="password")
            rmot_de_passe = st.text_input("Répéter le Mot de passe", type="password")

            if mot_de_passe == rmot_de_passe:
                submitted = st.form_submit_button("S'inscrire")
            else:
                st.warning("Les mots de passe ne correspondent pas.")

            if submitted:
                query = "INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe) VALUES (%s, %s, %s, %s)"
                values = (nom, prenom, email, mot_de_passe)  
                cursor.execute(query, values)
                db_connection.commit()
                st.success("Données insérées avec succès dans la base de données")

    elif choice == "Connection":
        st.title("Page Connection")
        # Logique du formulaire de connexion
        with st.form(key='connection_form'):
            st.subheader("Formulaire de Connection")
            email = st.text_input("Email (sans le @gmail.com)") + "@gmail.com"
            mot_de_passe = st.text_input("Mot de passe", type="password")
            submitted = st.form_submit_button("Se Connecter")
            if submitted:  # Assurez-vous de définir submitted dans votre logique de connexion
                query = "SELECT * FROM utilisateurs WHERE email = %s AND mot_de_passe = %s"
                values = (email, mot_de_passe)
                cursor.execute(query, values)
                result = cursor.fetchone()
                if result:
                    st.success("Connexion réussie !")
                    print(email + " est connecté")
                    db_connection.close()
                    art = 1  # Définir art à 1 après une connexion réussie
                    # st.experimental_rerun()  # Redémarrer Streamlit pour charger la page d'accueil
                    # if art == 1:
                    #     return  # Sortie de la fonction presentation()
                    #     home()  # Appel de la fonction home() après connexion réussie
    
    db_connection.close()

# Appel de la fonction presentation() pour démarrer l'application
presentation()





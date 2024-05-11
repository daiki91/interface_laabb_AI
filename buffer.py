import streamlit as st
from presentation.sql import get_db_connection
from home.home import home
import hashlib  # Pour le hachage des mots de passe

def presentation():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    st.sidebar.title("Menu")
    menu = ["Inscription", "Connexion"]
    choice = st.sidebar.selectbox("Choix", menu)

    if choice == "Inscription":
        st.title("Page Inscription")

        with st.form(key='inscription_form'):
            st.subheader("Formulaire d'Inscription")
            nom = st.text_input("Nom")
            prenom = st.text_input("Prénom")
            email = st.text_input("Email")
            mot_de_passe = st.text_input("Mot de passe", type="password")
            rmot_de_passe = st.text_input("Répéter le Mot de passe", type="password")

            if mot_de_passe == rmot_de_passe:
                submitted = st.form_submit_button("S'inscrire")
            else:
                st.warning("Les mots de passe ne correspondent pas.")

            if submitted:
                hashed_password = hashlib.sha256(mot_de_passe.encode()).hexdigest()
                query = "INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe) VALUES (%s, %s, %s, %s)"
                values = (nom, prenom, email, hashed_password)  
                try:
                    cursor.execute(query, values)
                    db_connection.commit()
                    st.success("Données insérées avec succès dans la base de données")
                except Exception as e:
                    st.error(f"Erreur lors de l'inscription : {str(e)}")

    elif choice == "Connexion":
        st.title("Page Connexion")
        with st.form(key='connexion_form'):
            st.subheader("Formulaire de Connexion")
            email = st.text_input("Email")
            mot_de_passe = st.text_input("Mot de passe", type="password")

            submitted = st.form_submit_button("Se Connecter")
            if submitted:
                hashed_password = hashlib.sha256(mot_de_passe.encode()).hexdigest()
                query = "SELECT * FROM utilisateurs WHERE email = %s AND mot_de_passe = %s"
                values = (email, hashed_password)
                cursor.execute(query, values)
                result = cursor.fetchone()
                if result:
                    st.success("Connexion réussie !")
                    home()
                else:
                    st.error("Connexion échouée. Email ou mot de passe incorrect.")

    db_connection.close()

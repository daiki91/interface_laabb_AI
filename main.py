import streamlit as st 
import mysql.connector
from presentation.presentation import presentation
from sidebar.sidebar import main
# def get_db_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="users"
#     )

# def main():
    # st.sidebar.title("Navigation")
    # selected_model = st.sidebar.radio("Choisir un modèle", ["Modèle 1", "Modèle 2", "Modèle 3", "Modèle 4"])

    # if selected_model == "Modèle 1":
    #     presentation()
    # elif selected_model == "Modèle 2":
    #     show_model_2()
    # elif selected_model == "Modèle 3":
    #     show_model_3()
    # elif selected_model == "Modèle 4":
    #     show_model_4()

# def presentation():
    # st.title("Modèle 1 : Inscription")
    # db_connection = get_db_connection()
    # cursor = db_connection.cursor()

    # if db_connection.is_connected():
    #     print("Connected to MySQL database")

    # menu = ["Inscription", "Connection"]
    # choice = st.sidebar.selectbox("Menu", menu)

    # if choice == "Inscription":
    #     st.title("Page Inscription")

    #     with st.form(key='inscription_form'):
    #         st.subheader("Formulaire d'Inscription")
    #         nom = st.text_input("Nom")
    #         prenom = st.text_input("Prénom")
    #         email = st.text_input("Email (sans le @gmail.com)") + "@gmail.com"
    #         mot_de_passe = st.text_input("Mot de passe", type="password")
    #         rmot_de_passe = st.text_input("Répéter le Mot de passe", type="password")

    #         if mot_de_passe == rmot_de_passe:
    #             submitted = st.form_submit_button("S'inscrire")
    #         else:
    #             st.warning("Les mots de passe ne correspondent pas.")

    #         if submitted:
    #             query = "INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe) VALUES (%s, %s, %s, %s)"
    #             values = (nom, prenom, email, mot_de_passe)  
    #             cursor.execute(query, values)
    #             db_connection.commit()
    #             st.success("Données insérées avec succès dans la base de données")

    # elif choice == "Connection":
    #     st.title("Page Connection")
    #     with st.form(key='connection_form'):
    #         st.subheader("Formulaire de Connection")
    #         email = st.text_input("Email (sans le @gmail.com)") + "@gmail.com"
    #         mot_de_passe = st.text_input("Mot de passe", type="password")

    #         submitted = st.form_submit_button("Se Connecter")
    #         if submitted:
    #             query = "SELECT * FROM utilisateurs WHERE email = %s AND mot_de_passe = %s"
    #             values = (email, mot_de_passe)
    #             cursor.execute(query, values)
    #             result = cursor.fetchone()
    #             if result:
    #                 st.success("Connexion réussie !")
    #             else:
    #                 st.error("Connexion échouée. Email ou mot de passe incorrect.")

    # db_connection.close()

def show_model_2():
    st.title("Modèle 2 : ...")
    # Contenu du modèle 2

def show_model_3():
    st.title("Modèle 3 : ...")
    # Contenu du modèle 3

def show_model_4():
    st.title("Modèle 4 : ...")
    # Contenu du modèle 4

if __name__ =="__main__":
    main()

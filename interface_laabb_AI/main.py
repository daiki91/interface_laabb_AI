import streamlit as st 
import mysql.connector
from presentation.presentation import presentation
from sidebar.sidebar import main
from home.home import home



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

import streamlit as st 
from presentation.sql import get_db_connection
from presentation.presentation import presentation
from sidebar.sidebar import main
from home.home import home



# def show_model_2():
#     st.title("Modèle 2 : ...")
#     # Contenu du modèle 2

# def show_model_3():
#     st.title("Modèle 3 : ...")
#     # Contenu du modèle 3

# def show_model_4():
#     st.title("Modèle 4 : ...")
#     # Contenu du modèle 4
a=0
presentation()
if a == 1:
    home()


if __name__ =="__main__":
    main()

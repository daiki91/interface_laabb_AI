import  streamlit as st
from presentation.presentation  import presentation

def main():
    # st.sidebar.title("Navigation")
    # selected_model = st.sidebar.radio("Choisir un modèle", ["presentation", "Modèle 2", "Modèle 3", "Modèle 4"])

    # if selected_model == "presentation":
        presentation()
    # elif selected_model == "Modèle 2":
    #     show_model_2()
    # elif selected_model == "Modèle 3":
    #     show_model_3()
    # elif selected_model == "Modèle 4":
    #     show_model_4()
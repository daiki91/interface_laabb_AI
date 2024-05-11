#when we import hydralit, we automatically get all of Streamlit
import hydralit as hy
import streamlit as st
import hydralit_components as hc
# from sidebar.sidebar import get_selected_model


app = hy.HydraApp(title='Secure Hydralit Data Explorer',
                  favicon="🚀",hide_streamlit_markers=True,
                  use_navbar=True, navbar_sticky=True,
                #   banner_spacing=[30,20,40,30,10]
                  )

@app.addapp()
def home():
    # image lambtech
    # st.image('./iibs.png')
    # Définition du style CSS pour les cartes
    st.markdown(
        """
        <style>
        .card {
            padding: 20px 20px 20px 70px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            background-color: #F4EFEF;
            transition: box-shadow 0.3s ease;
        }
        .card:hover {
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    with col1:
    # Define the card content as HTML string
        ml_description = "Description ou contenu lié au Machine Learning."
        card_content = f"""
        <div class="card">
            <h3>Machine Learning</h3>
            <p>{ml_description}</p>
        </div>
        """
        st.markdown(card_content, unsafe_allow_html=True)
    with col2:
    # Define the card content as HTML string
        ml_description = "Description ou contenu lié au Machine Learning  ."
        card_content = f"""
        <div class="card">
            <h3>Machine Learning</h3>
            <p>{ml_description}</p>
        </div>
        """
        st.markdown(card_content, unsafe_allow_html=True)

        br_content = f"""
        <div >
            <br>
        </div>
        """
        st.markdown(br_content, unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        ml_description = "Description ou contenu lié au Machine Learning."
        card_content = f"""
        <div class="card">
            <h3>Machine Learning</h3>
            <p>{ml_description}</p>
        </div>
        """
        st.markdown(card_content, unsafe_allow_html=True)
    with col4:
    # Define the card content as HTML string
        ml_description = "Description ou contenu lié au Machine Learning."
        card_content = f"""
        <div class="card">
            <h3>Machine Learning</h3>
            <p>{ml_description}</p>
        </div>
        """
        st.markdown(card_content, unsafe_allow_html=True)
    
 

@app.addapp(title='Accueil')
# @app.addapp(title='AI_n_BD', icon="🥰")
def model1():
    hy.info('Hello form accueil')
@app.addapp(title='Modele 2')
def model2():
    hy.info('Hello form modele 2')

# #Le sidebar 
# selected_model = get_selected_model()
# if selected_model == "model1":
#     model1()
# elif selected_model == "model2":
#     model2()
# else:
#   # Display default content if no model is selected
#   st.write("Please select a model from the sidebar.")

app.run()

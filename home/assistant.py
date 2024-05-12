import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os 

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
# Initialisez votre client OpenAI
client = OpenAI()

def main():
    st.title("Assistant **AGRISEN**(Recommandations)")
    st.write("""
Bienvenue à bord de notre **AGRISEN** d'assistant agronomique ! 
             Conçu pour simplifier votre expérience d'agriculteur, notre **AGRISEN** répond à vos questions sur l'irrigation, la fertilisation et les traitements phytosanitaires, 
             vous guide vers les meilleures pratiques agricoles""")

    # Zone de texte pour que l'utilisateur saisisse son message
    user_input = st.chat_input("Vous: ")

    if user_input is not None:
        # Appel à l'API OpenAI pour obtenir la réponse de l'assistant
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """Vous êtes un assistant **AGRISEN** conçu pour aider les agriculteurs en leur fournissant des recommandations sur l'irrigation, la fertilisation, les
                    traitements phytosanitaires et les meilleures pratiques agricoles. """},
                {"role": "user", "content": user_input}
            ]
        )

        # Afficher la réponse de l'assistant
        assistant_response = completion.choices[0].message.content
        st.write("vous:",user_input)
        st.write("**AGRISEN**: ", assistant_response)
def risque():
    st.title("Assistant **AGRISEN**(Risques Climatiques et Agricoles)")
    st.write("""
Bienvenue à bord de notre **AGRISEN** d'assistant agronomique !
              Conçu pour simplifier votre expérience d'agriculteur, notre **AGRISEN** répond à vos questions sur les Risques Climatiques et Agricoles, 
             vous guide vers les meilleures pratiques agricoles""")

    # Zone de texte pour que l'utilisateur saisisse son message
    user_input = st.chat_input("Vous: ")

    if user_input is not None:
        # Appel à l'API OpenAI pour obtenir la réponse de l'assistant
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """Vous êtes un assistant **AGRISEN** conçu pour aider les agriculteurs en leur fournissant des idees  sur les Risques Climatiques et Agricoles 
                    traitements phytosanitaires et les meilleures pratiques agricoles. """},
                {"role": "user", "content": user_input}
            ]
        )

        # Afficher la réponse de l'assistant
        assistant_response = completion.choices[0].message.content
        st.write("vous:",user_input)
        st.write("**AGRISEN**: ", assistant_response)

if __name__ == "__main__":
    main()

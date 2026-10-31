import streamlit as st
import google.generativeai as genai

st.title("⚽ Bot di Analisi Calcistica")
st.write("Inserisci la tua chiave API e analizza qualsiasi partita in pochi secondi!")

# Barra laterale per la chiave API
api_key = st.sidebar.text_input("Inserisci la tua API Key di Google AI Studio", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    squadra_casa = st.text_input("Squadra di Casa", "Inter")
    squadra_trasferta = st.text_input("Squadra in Trasferta", "Juventus")
    statistiche = st.text_area("Dati e statistiche della partita", "Inter in casa media xG 1.8. Juventus difesa solida.")

    if st.button("Genera Analisi Tattica"):
        with st.spinner("L'intelligenza artificiale sta analizzando la partita..."):
            prompt = f"""
            Sei un match analyst professionista. Analizza questa partita in modo tecnico e oggettivo:
            Partita: {squadra_casa} vs {squadra_trasferta}
            Dati e statistiche: {statistiche}

            Fornisci:
            1. Analisi Tattica
            2. Metriche e xG stimati
            3. Punti di Forza e Debolezza
            4. Pronostico Motivato
            """
            response = model.generate_content(prompt)
            st.markdown(response.text)
else:
    st.warning("👈 Inserisci la tua chiave API nella barra laterale sinistra per sbloccare il bot.")

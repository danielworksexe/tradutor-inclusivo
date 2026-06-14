import streamlit as st
import google.generativeai as genai

# Configuração da página Streamlit
st.set_page_config(page_title="Tradutor de Textos para Alfabetização", page_icon="📖")

# Configurar a chave da API (o usuário deve inserir a sua própria chave de forma segura)
# Para fins do projeto, você pode colocar st.secrets ou pedir na interface
api_key = st.text_input("Insira sua API Key do Google Gemini:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    st.title("📖 Tradutor Escolar Inclusivo")
    st.write("Bem-vindo! Cole um aviso da escola abaixo e eu vou simplificá-lo para facilitar a leitura de quem está aprendendo a ler.")

    texto_original = st.text_area("Cole o aviso escolar aqui:", height=200)

    if st.button("Simplificar Texto"):
        if texto_original:
            with st.spinner("Simplificando o texto..."):
                prompt = f"Reescreva o seguinte texto escolar para uma pessoa adulta que está em processo de alfabetização. Use palavras simples, frases curtas e diretas. Evite termos técnicos ou burocráticos. Texto original: {texto_original}"
                
                try:
                    response = model.generate_content(prompt)
                    st.success("Texto Simplificado!")
                    st.write("### Resultado:")
                    st.info(response.text)
                except Exception as e:
                    st.error(f"Erro ao processar: {e}")
        else:
            st.warning("Por favor, insira um texto para ser simplificado.")
else:
    st.warning("Por favor, insira a chave da API do Google Gemini para continuar.")

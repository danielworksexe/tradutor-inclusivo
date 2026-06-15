import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import io

# Configuração da página Streamlit
st.set_page_config(page_title="Tradutor Escolar Inclusivo", page_icon="📖")

# Tentar puxar a chave de API dos Segredos do Streamlit
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-3.5-flash')
except KeyError:
    st.error("Erro: Chave de API não configurada nos segredos do sistema.")
    st.stop()

st.title("📖 Tradutor Escolar Inclusivo")
st.write("Bem-vindo! Cole um aviso da escola abaixo e eu vou simplificá-lo para facilitar a leitura.")

texto_original = st.text_area("Cole o aviso escolar aqui:", height=200)

if st.button("Simplificar Texto"):
    if texto_original:
        with st.spinner("Simplificando o texto..."):
            prompt = f"Reescreva o seguinte texto escolar para uma pessoa adulta que está em processo de alfabetização. Use palavras simples, frases curtas e diretas. Evite termos técnicos ou burocráticos. Texto original: {texto_original}"
            
            try:
                # 1. Gerar o texto simplificado
                response = model.generate_content(prompt)
                texto_simplificado = response.text
                
                st.success("Texto Simplificado!")
                st.write("### Resultado:")
                st.info(texto_simplificado)
                
                # 2. Gerar o áudio do texto simplificado
                with st.spinner("Gerando áudio..."):
                    tts = gTTS(text=texto_simplificado, lang='pt')
                    audio_bytes = io.BytesIO()
                    tts.write_to_fp(audio_bytes)
                    audio_bytes.seek(0)
                    
                    st.write("### Ouça o aviso:")
                    st.audio(audio_bytes, format='audio/mp3')
                    
            except Exception as e:
                st.error(f"Erro ao processar a inteligência artificial: {e}")
    else:
        st.warning("Por favor, insira um texto para ser simplificado.")

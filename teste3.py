import streamlit as st 
import subprocess
import os

st.title('transcription.app')
extensions = ['json', 'srt', 'txt', 'vtt', 'tsv']


# Upload do arquivo de áudio
audio_file = st.file_uploader('Carregar Audio', type=['wav', 'mp3', 'mp4a'])

# Botão para iniciar a transcrição
if st.button('Transcrever Áudio') and audio_file:
    
    

    # Salvar o arquivo carregado no disco com o nome desejado
    with open("audioteste.mp3", "wb") as f:
        f.write(audio_file.getbuffer())

   

        for ext in extensions:
            filename = f"audioteste.{ext}"
            if os.path.exists(filename):
                os.remove(filename)
            else:
                pass    

    # Comando a ser executado
    command = ["whisper", "audioteste.mp3", "--model", "medium", "--language", "pt"]

    # Executando o comando
    subprocess.run(command)

    # Remover o arquivo de áudio após a transcrição
    os.remove("audioteste.mp3")

    # Apresenta links de download e visualização para cada arquivo gerado
    for ext in extensions:
        filename = f"audioteste.{ext}"
        if os.path.exists(filename):
            st.markdown(f"### Arquivo {ext.upper()}:")
            st.markdown(f"**Baixar {ext.upper()}:**")
            st.download_button(label=f"Download {ext.upper()}", data=open(filename, 'rb'), file_name=filename, mime=None, key=None, help=None, on_click=None)
            st.markdown(f"**Visualizar {ext.upper()}:**")
            with open(filename, 'r', encoding='utf-8') as file:
                st.code(file.read())

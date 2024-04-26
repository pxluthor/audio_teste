import streamlit as st
import subprocess
import os
import shutil

st.title('transcription.app')

extensions = ['json', 'srt', 'txt', 'vtt', 'tsv']

# Upload do arquivo de áudio
audio_file = st.file_uploader('Carregar Audio', type=['wav', 'mp3', 'mp4a'])

# Botão para iniciar a transcrição
if st.button('Transcrever Áudio') and audio_file:
    # Nome do arquivo original
    original_filename = os.path.splitext(audio_file.name)[0]

    # Salvar o arquivo carregado no disco com o mesmo nome do arquivo original
    audio_path = os.path.join("arquivos", audio_file.name)
    with open(audio_path, "wb") as f:
        f.write(audio_file.getbuffer())

    # Comando a ser executado
    command = ["whisper", audio_path, "--model", "medium", "--language", "pt"]

    # Executando o comando
    subprocess.run(command)

    # Mover os arquivos transcritos para a pasta "arquivos"
    for ext in extensions:
        filename = f"{original_filename}.{ext}"
        if os.path.exists(filename):
            # Novo nome com base no nome do arquivo original
            new_filename = f"{original_filename}.{ext}"
            shutil.move(filename, os.path.join("arquivos", new_filename))

    # Apresenta links de download e visualização para cada arquivo gerado
    for ext in extensions:
        filename = os.path.join("arquivos", f"{original_filename}.{ext}")
        if os.path.exists(filename):
            st.markdown(f"### Arquivo {ext.upper()}:")
            st.markdown(f"**Baixar {original_filename}.{ext}:**")
            st.download_button(label=f"Download {ext.upper()}", data=open(filename, 'rb'), file_name=filename, mime=None, key=None, help=None, on_click=None)
            st.markdown(f"**Visualizar {ext.upper()}:**")
            with open(filename, 'r', encoding='utf-8') as file:
                st.text_area(f"Conteúdo do arquivo {ext.upper()}:", value=file.read(), height=200)



'''
nomes dos arquivos iguais 

'''
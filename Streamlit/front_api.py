import cv2
import numpy as np
import streamlit as st
import requests
from PIL import Image
import io
import base64

def get_image_download_link(img,filename,text):
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href

def blur_faces_api(img: np.ndarray) -> np.ndarray:
    API_ENDPOINT = "https://nti7y6pgge.execute-api.us-east-2.amazonaws.com/desenvolvimento"
    # Codifica a imagem para formato PNG em bytes
    is_success, im_buf_arr = cv2.imencode(".png", img)
    if not is_success:
        raise Exception("Não foi possível codificar a imagem para o formato PNG")
    byte_im = im_buf_arr.tobytes()

    # Envia a imagem codificada para a API e recebe a resposta
    response = requests.post(url=API_ENDPOINT, data=byte_im)
    if response.status_code != 200:
        raise Exception(f"Falha na requisição à API: {response.status_code}")

    # Lê a imagem diretamente da resposta como um array NumPy
    img_corrected = np.frombuffer(response.content, np.uint8)
    img_corrected = cv2.imdecode(img_corrected, cv2.IMREAD_COLOR)

    return img_corrected

def convert_uploaded_file_to_cv2_image(uploaded_file):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    return img

def main():
    left_co, cent_co,last_co = st.columns(3)
    
    st.image('Logo Site.png')
        
    st.title("  Aplicativo de Desfoque de Rostos")
    
    # Texto descritivo abaixo do título
    st.markdown('<div style="text-align: justify;">Este é um aplicativo projetado para ser utilizado como tarefa final da Especialização em Visão Computacional, ministrado por Carlos Melo, através da Escola Sigmoidal. Nele encontram-se conceitos de detecção de rostos, fitltros, manipulação de imagens, bem como toda configuração para uso de uma Função Lambda via API Gateway. Está disponibilizado no link do repositório bem como descrito detalhadamente no post do blog Natural Engines.</div>', unsafe_allow_html=True)
        
    # Adiciona o informações na sidebar
    st.sidebar.image('teste.png')
    st.sidebar.link_button('Estimativa de velocidade de carros com Yolo', 'https://www.naturalengines.com/post/estimativa-de-velocidade-de-carros-com-yolo')
    st.sidebar.link_button('Treinamento de Modelo para Classificação de Imagens', 'https://www.naturalengines.com/post/treinamento-de-modelo-para-classifica%C3%A7%C3%A3o-de-imagens')
    st.sidebar.link_button('Manuseio e Processamento de Imagens', 'https://www.naturalengines.com/post/manuseio-e-processamento-b%C3%A1sico-de-imagens')
    st.sidebar.link_button('Geometria Primitiva e Transformações 2D com Python', 'https://www.naturalengines.com/post/geometria-primitiva-e-transforma%C3%A7%C3%B5es-2d-com-python')
    st.sidebar.link_button('Python e Ténica de Keying', 'https://www.naturalengines.com/post/python-e-t%C3%A9cnica-de-keying')
    st.sidebar.link_button('LinkedIn', 'https://www.linkedin.com/in/vinicius-goia-75a403234')
    
    uploaded_file = st.file_uploader("Escolha uma imagem para desfoque de rostos (max 2,5MB)", type=["png", "jpg", "jpeg"])
    
    st.image('teste2_gif.gif')

    if uploaded_file is not None:
        # Convertendo a imagem carregada para um formato que a API pode processar
        img_original = convert_uploaded_file_to_cv2_image(uploaded_file)

        # Aplicando o desfoque de rostos
        try:
            img_deskewed = blur_faces_api(img_original)

            # Convertendo imagens de BGR para RGB para exibição
            img_original_rgb = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)
            img_blurred = cv2.cvtColor(img_deskewed, cv2.COLOR_BGR2RGB)

            # Exibindo imagens lado a lado
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_original_rgb, caption="Imagem Original", use_column_width=True)
            with col2:
                st.image(img_blurred, caption="Imagem Desfocada", use_column_width=True)
                
                ## Original image came from cv2 format, fromarray convert into PIL format
                result = Image.fromarray(img_blurred)
                st.markdown(get_image_download_link(result,'img_blurred.png','Download img_blurred'), unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"Erro ao processar a imagem: {e}")
            


if __name__ == "__main__":
    main()
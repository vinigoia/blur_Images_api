import cv2
import base64
import numpy as np
import dlib
import imutils
from imutils import face_utils
from scipy.ndimage import filters
from PIL import Image


def encode_image_to_base64(
        img: np.ndarray
        ) -> str:
    """
    Codifica uma imagem (array da NumPy) diretamente para a representação em string Base64, 
    salvando temporariamente em um arquivo.

    Args:
        img (np.ndarray): A imagem como um array da NumPy para ser codificada.

    Returns:
        str: A representação da imagem codificada em Base64.
    """
    # Caminho temporário para salvar a imagem
    aux_path = '/tmp/tmp_image.png'
    # Salva a imagem no caminho temporário
    cv2.imwrite(aux_path, img)

    # Abre a imagem salva, codifica em Base64, e retorna a string decodificada
    with open(aux_path, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode("utf-8")

    return encoded_string


def decode_base64_to_image(
        encoded_string: str,
        img_path: str = "/tmp/decoded_img.png"
        ) -> np.ndarray:
    """
    Decodifica uma string Base64 para uma imagem e salva como arquivo, então lê a imagem do arquivo e retorna como um array da NumPy.

    Args:
        encoded_string (str): String Base64 da imagem a ser decodificada.
        img_path (str): Caminho do arquivo onde a imagem decodificada será salva. Modificado para /tmp/decoded_img.png

    Returns:
        np.ndarray: A imagem decodificada como um array da NumPy.
    """

    img_data = base64.b64decode(encoded_string)
    with open(img_path, "wb") as image_file:
        image_file.write(img_data)

    image = cv2.imread(img_path)
    return image


def blur_faces(image):
    """
    Identifica e desfoca as faces de pessoas.

    Parâmetros:
        image (numpy.ndarray): Imagem para desfocar.

    Retorna:
        numpy.ndarray: Imagem desfocada.
    """
    
    #Instanciamento de métodos de detecção facial   
    face_detector = dlib.get_frontal_face_detector()
    predict_points = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    #Leitura da Imagem
    img = image

    #Conversão da imagem em escala de cinza
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #Conversão da imagem para padrão PIL
    pil_im = Image.fromarray(img) 
    
    #Aplicação do método na imagem em escala de cinza
    rects = face_detector(gray_image, 1)
    
    #Listas de coordenadas vazias
    x1=[]
    y1=[]
    w1=[]
    h1=[]

    #Iteração nos dados adquiridos
    for (i, rect) in enumerate(rects):
        reference_points= predict_points(gray_image, rect)
        reference_points = face_utils.shape_to_np(reference_points)
        
        # (x, y, w, h)
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        x1.append(x)
        y1.append(y)
        w1.append(w)
        h1.append(h)
        
        #Definição de área para recorte
        box = (x, y, (x+w),(y+h)) 
        
        #Recorte da imagem
        region = pil_im.crop(box) 
        
        #Aplicação de filtro gaussiano para desfoque
        gauss_face = filters.gaussian_filter(region,10) 
        
        #Transformação para padrão PIL
        gauss_face = Image.fromarray(gauss_face)
        
        #Colagem das faces desfocadas na imagem original
        pil_im.paste(gauss_face,box) #usar 
        
    #Tranformação em Array   
    pil_im = np.array(pil_im)
    
    #Desenho da caixa de demarcação
    for i,n in enumerate(x1):
        cv2.rectangle(pil_im, (x1[i], y1[i]), (x1[i] + w1[i], y1[i] + h1[i]), (0, 150, 200), 2) 
        
    return pil_im


def lambda_handler(event, context):
    # Exemplo de como obter a string base64 da imagem a partir do evento
    base64_string = event['body']

    # Decodifica a string base64 para uma imagem
    image = decode_base64_to_image(base64_string)

    # Aplica a correção de inclinação na imagem
    processed_image = blur_faces(image)

    # Codifica a imagem processada em Base64
    processed_image_base64 = encode_image_to_base64(processed_image)

    # Retorna a imagem processada codificada em Base64
    return {
        'statusCode': 200,
        'isBase64Encoded': True,
        'headers': {'Content-Type': 'image/png'},
        'body': processed_image_base64
    }

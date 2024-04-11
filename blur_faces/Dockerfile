# Usando a imagem base oficial do Python 3.11 para AWS Lambda
FROM public.ecr.aws/lambda/python:3.11

# Copia arquivos pertinenetes
#COPY dlib-19.24.1-cp311-cp311-win_amd64.whl ./
COPY shape_predictor_68_face_landmarks.dat ./

# Instala as dependências necessárias
#RUN apt-get install -y build-essential cmake
RUN pip install numpy requests opencv-python-headless Pillow imutils scipy dlib-bin
#RUN pip install ./dlib-19.24.1-cp311-cp311-win_amd64.whl  

# Copia o código da função para o contêiner
COPY lamb_func.py ./

# Define o comando para executar a função lambda
CMD ["lamb_func.lambda_handler"]
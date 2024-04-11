<div align="center">
  
  [![Linkedin Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/vinicius-goia-75a403234)](https://www.linkedin.com/in/vinicius-goia-75a403234)
  [![Instagram Badge](https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/viniciusgoia/)


</div>

# Desfoque de Rostos

Este repositório refere-se ao projeto de finalização do Curso de Especialização em Visão Computacional, ministrado por Carlos Melo, da Escola Sigmoidal. O projeto tem o objetivo de exemplificar uma aplicação de ponta a ponta, 
desde o desenvolvimento das funções até o deploy na AWS, utilizando as ferramentas Lambda Function e API Gateway da plataforma. A aplicação em si utiliza conceitos de detecção de faces, utilização de filtros e manipulação de imagens, com o intuito de 
encontrar e desfocar faces de pessoas em fotos.

## Pré-requisitos

* **VSCode** - Editor de código utilizado durante o desenvolvimento. Disponível para Windows, macOS e Linux. [Instalação oficial do VSCode](https://code.visualstudio.com/download)

* **Pyenv** - Ferramenta para gerenciar múltiplas versões do Python. A versão recomendada do Python para este projeto é a `3.11.3`. [Instruções oficiais de instalação do Pyenv](https://github.com/pyenv/pyenv#installation)

* **Poetry** - Ferramenta de gerenciamento de dependências em Python. [Instruções oficiais de instalação do Poetry](https://python-poetry.org/docs/#installation)

* **Git** - Ferramenta de controle de versão distribuído. [Instruções oficiais de instalação do Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

* **GitHub** - Plataforma de hospedagem de código. É essencial ter uma conta para interagir com os repositórios. [Como criar uma conta no GitHub](https://docs.github.com/pt/get-started/onboarding/getting-started-with-your-github-account)

## Instalação e Configuração

Aqui está um resumo dos passos que você precisa seguir:

1. Clonar o [Repositório Github](https://github.com/vinigoia/blur_Images_api) para a sua máquina local e acessar a pasta `blur_Images_api`:

   ```bash
   git clone https://github.com/vinigoia/blur_Images_api.git
   cd blur_Images_api
   ```

2. Configurar o Poetry para criar ambientes virtuais dentro do diretório do projeto.

   ```bash
   poetry config virtualenvs.in-project true
   ```

3. Configurar a versão `3.11.3` do Python com Pyenv:

   ```bash
   pyenv install 3.11.3
   pyenv local 3.11.3
   ```

4. Instalar as dependências do projeto:

   ```bash
   poetry install
   ```

5. Ativar o ambiente virtual.

   ```bash
   poetry shell
   ```

6. Testando sua instalação

   Após seguir os passos de instalação e configuração, execute os testes para garantir que tudo está funcionando como esperado:

   ```bash
   task test
   ```

7. Executar Streamlit

   Executar arquivo com os códigos do Streamlit para iniciar aplicação:

   ```bash
   cd Streamlit
   streamlit run front_api.py      
   ```

Neste ponto, seu navegador padrão será aberto e a aplicação se iniciará. Você pode testá-la realizando o upload de uma imagem até 2.5Mb, e baixando logo em seguida após o processamento.


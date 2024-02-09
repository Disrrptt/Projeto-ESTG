import requests
from bs4 import BeautifulSoup

def extrair_nomes_usuarios(url_base, num_paginas):
    contador = 1
    for pagina in range(1, num_paginas + 1):
        url = f"{url_base}&pagina={pagina}"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            soup = BeautifulSoup(resposta.text, 'html.parser')
            usuarios_items = soup.find_all('li', class_='lista-resultados__item')
            for item in usuarios_items:
                status = item.find('span', class_='lista-resultados__info-exercicio atuando')
                if status != None:
                    nome_usuario = item.find('a').text.strip()  
                    print(f"{contador} - {nome_usuario}")
                    contador += 1
                
url_base = 'https://www.camara.leg.br/deputados/quem-sao/resultado?search=&partido=&uf=&legislatura=57&sexo='
num_paginas = 23

extrair_nomes_usuarios(url_base, num_paginas)

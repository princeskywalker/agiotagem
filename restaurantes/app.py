import requests
from pprint import pprint
url="https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)
if response.status_code ==200: print('Json Capturado...')
else: print('erro')
if response.status_code == 200:
    dados = response.json()
    dados_restautante={}
    print(dados[0])
    for item in dados:

        nome_restaurante = item['Company']

        if nome_restaurante not in dados_restautante:
            dados_restautante[nome_restaurante] = []


        dados_restautante[nome_restaurante].append({
            'item': item['Item'],
            'price':item['price'],
           'description':item['description']

       })
        print(dados_restautante)
        # {'Company': 'McDonald’s', 'Item': 'Hamburger', 'price': 32.42,
    #  'description': 'Uma explosão de sabores em cada mordida.'}



else:print("Erro")
# "FABRICIO NOU"
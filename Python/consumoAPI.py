def cep():
#~ API básica para verificar cep

    import requests

    cep = input("DIGITE O CEP: ")
    url = f"https://viacep.com.br/ws/{cep}/json/"

    resposta = requests.get(url)
    dados = resposta.json()

    if "erro" not in dados:
        print(f'Cidade: {dados["localidade"]}/{dados["uf"]}')
        print(f'{dados["logradouro"]}/{dados["bairro"]}')
    else:
        print('CEP inválido')
#cep()        
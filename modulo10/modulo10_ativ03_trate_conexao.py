import requests

url = "https://api.exemplo.com/dados"

try:
    # Define um tempo limite (timeout) para evitar travamentos em conexões lentas
    resposta = requests.get(url, timeout=5)
    
    # Lança uma exceção caso a API retorne um erro HTTP (ex: 404, 500)
    resposta.raise_for_status()
    
    # Tenta converter a resposta para JSON
    dados = resposta.json()
    print("Dados recebidos com sucesso:", dados)

except requests.exceptions.Timeout:
    print("Erro: A conexão demorou muito para responder (conexão lenta).")

except requests.exceptions.HTTPError as erro_http:
    print(f"Erro HTTP retornado pela API: {erro_http}")

except requests.exceptions.ConnectionError:
    print("Erro: Falha na conexão de rede. Verifique sua internet ou a URL.")

except ValueError:
    print("Erro: A resposta recebida da API não é um JSON válido.")

except requests.exceptions.RequestException as erro:
    print(f"Ocorreu um erro inesperado na requisição: {erro}")
import requests

def buscar_filme(nome_filme, api_key):
    url = "https://api.themoviedb.org/3/search/movie"
    
    # Parâmetros da requisição HTTP
    params = {
        "api_key": api_key,
        "query": nome_filme,
        "language": "pt-BR"  # Retorna título e sinopse em português
    }

    try:
        # Faz a requisição GET com timeout para conexões lentas
        resposta = requests.get(url, params=params, timeout=5)
        resposta.raise_for_status()
        
        dados = resposta.json()
        resultados = dados.get("results", [])

        if not resultados:
            print("Nenhum filme encontrado com esse nome.")
            return

        # Pega o primeiro resultado retornado pela busca
        filme = resultados[0]

        titulo = filme.get("title", "Sem título")
        data_lancamento = filme.get("release_date", "Data não informada")
        sinopse = filme.get("overview", "Sinopse não disponível.")
        
        # Exibe os dados formatados
        print("\n--- Informações do Filme ---")
        print(f"Título: {titulo}")
        print(f"Lançamento: {data_lancamento}")
        print(f"Sinopse: {sinopse}")

    except requests.exceptions.Timeout:
        print("Erro: A requisição demorou muito para responder.")
    except requests.exceptions.HTTPError as erro:
        print(f"Erro HTTP na API: {erro}")
    except requests.exceptions.RequestException as erro:
        print(f"Erro de conexão: {erro}")

# Exemplo de uso:
# Substitua 'SUA_CHAVE_API_AQUI' pela chave obtida no site do TMDB
API_KEY = "SUA_CHAVE_API_AQUI"
filme_busca = input("Digite o nome de um filme: ")

buscar_filme(filme_busca, API_KEY)

#import requests


API_URL = "https://api.tvmaze.com"


def buscar_serie(nome):
    url = f"{API_URL}/search/shows"
    parametros = {"q": nome}
    try:
        resposta = requests.get(url, params=parametros, timeout=10)
        resposta.raise_for_status()
        resultados = resposta.json()
        return resultados

    except requests.exceptions.RequestException as erro:
        print(f"Erro ao consultar a API: {erro}")
        return []

def exibir_resultados(resultados):
    if not resultados:
        print("Nenhuma série encontrada.")
        return

    for resultado in resultados:
        serie = resultado["show"]

        print("-" * 40)
        print(f"Nome: {serie.get('name', 'Não informado')}")
        print(f"Idioma: {serie.get('language', 'Não informado')}")
        print(f"Gêneros: {', '.join(serie.get('genres') or [])}")
        print(f"Status: {serie.get('status', 'Não informado')}")
        print(f"Estreia: {serie.get('premiered', 'Não informado')}")
        print(f"Site: {serie.get('url', 'Não informado')}")

        resumo = serie.get("summary") or "Sinopse indisponível."
        print(f"Sinopse: {resumo}")

def main():
    nome = input("Digite o nome de uma série: ").strip()

    if not nome:
        print("Você precisa informar um nome.")
        return

    resultados = buscar_serie(nome)
    exibir_resultados(resultados)

if __name__ == "__main__":
    main()

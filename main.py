import requests

# URL de la API
url = "https://nerdyhub-514430211337.us-central1.run.app/api/threads"

try:
    # Realizar la solicitud GET
    response = requests.get(url)

    # Verificar el código de estado HTTP
    if response.status_code == 200:
        # Obtener los datos en formato JSON
        data = response.json()  # Imprimir los datos
    else:
        print(f"Error en la solicitud. Código de estado: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error al conectar con la API: {e}")


def org(data):
    organized_by_hashtags = {}
    for thread in data:
        hashtags = thread['hashtags']
        if not hashtags:  # Si no tiene hashtags, agrupar en "Sin Hashtags"
            organized_by_hashtags.setdefault("Sin Hashtags", []).append(thread)
        else:
            for hashtag in hashtags:
                organized_by_hashtags.setdefault(hashtag, []).append(thread)

    # Organizar por likes dentro de cada grupo de hashtags
    for hashtag, threads in organized_by_hashtags.items():
        organized_by_hashtags[hashtag] = sorted(threads, key=lambda x: x['likes'], reverse=True)

    # Mostrar los resultados organizados
    for hashtag, threads in organized_by_hashtags.items():
        print(f"\n### Hashtag: {hashtag}")
        for thread in threads:
            print(f"- {thread['title']} ({thread['likes']} likes)")

org(data)
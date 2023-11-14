from django.shortcuts import render
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def pokemon_detail(request, name):
    """
    Vista(GET) para mostrar información detallada sobre un Pokémon específico.
    
    Parámetros:
        - request: Objeto de solicitud HTTP.
        - name: Nombre del Pokémon del que se desea obtener información.
    
    Retorna:
        - Plantilla HTML(pokemon_detail.html) renderizada que muestra los detalles del Pokémon si se encuentra.
    """

    api_url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
    response = requests.get(api_url)

    if response.status_code == 200:
        # Si la solicitud es exitosa, extrae la información y habilidades del Pokémon
        info = response.json()
        abilities = [ability["ability"]["name"] for ability in info["abilities"]]
        image = info["sprites"]["front_default"]
        return render(
            request,
            "pokemon_detail.html",
            {"info": info, "abilities": abilities, "image": image},
        )
    else:
        # Si no se puede obtener la información del Pokémon, muestra un mensaje de error
        return render(request, {"mensaje": "No se pudo mostrar el Pokémon"})


def pokemon_lista(request):
    """
    Vista (GET) para mostrar una lista paginada de Pokémon.
    
    Parámetros:
        - request: Objeto de solicitud HTTP.
    
    Retorna:
        - Plantilla HTML renderizada que muestra una lista de Pokémon con paginación.
    """
    api_url = "https://pokeapi.co/api/v2/pokemon/"
    response = requests.get(api_url)

    if response.status_code == 200:
        # Si la solicitud es exitosa, obtiene los datos de la lista de Pokémon.
        data = response.json()
        pokemon_list = []

        # Obtiene datos individuales de cada Pokémon en la lista.
        pokemon_data = [
            requests.get(pokemon["url"]).json() for pokemon in data["results"]
        ]
        
        # Pagina los datos, mostrando 6 Pokémon por página.
        paginator = Paginator(pokemon_data, 6)
        page = request.GET.get("page")
        try:
            pokemon_page = paginator.page(page)
        except PageNotAnInteger:
            pokemon_page = paginator.page(1)
        except EmptyPage:
            pokemon_page = paginator.page(paginator.num_pages)

        # Prepara la información necesaria para mostrar en la plantilla
        for pokemon in pokemon_page:
            pokemon_info = {
                "name": pokemon["name"],
                "image": pokemon["sprites"]["front_default"],
            }
            pokemon_list.append(pokemon_info)

        # Renderiza la plantilla con la lista de Pokémon paginada
        return render(
            request,
            "pokemon.html",
            {"pokemon_list": pokemon_list, "pokemon_page": pokemon_page},
        )
    else:
        return render(request, {"msj_error": "No se pudo obtener la lista de Pokémon"})

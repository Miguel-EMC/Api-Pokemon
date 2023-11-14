# Proyecto Pokémon API con Django Rest Framework

Este proyecto utiliza Django Rest Framework para obtener datos de la Pokémon Public API y mostrarlos a través de una API propia.

**API** : [Api Pokémon](https://pokeapi.co/api/v2/pokemon)

## Instalación

1. Clonar este repositorio: `git clone URL_DEL_REPOSITORIO`
2. Crear y activar un entorno virtual:
   - `python -m venv env`
   - Windows: `nombre_entorno\Scripts\activate`
   - macOS y Linux: `source nombre_entorno/bin/activate`
3. Instalar las dependencias: `pip install -r requirements.txt`
4. Instalar django: `pip install django`
5. Realizar las migraciones: `python manage.py migrate`

## Uso

1. Ejecuta el servidor: `python manage.py runserver`
2. Accede a la API en `http://localhost:8000/api/` para ver la lista de Pokémon.
3. Para obtener detalles de un Pokémon específico, visita `http://localhost:8000/pokemon/<name>/`.

## Autor

- [Miguel Muzo](https://github.com/Miguel-EMC)

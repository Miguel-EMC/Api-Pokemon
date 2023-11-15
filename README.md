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

## Detalles del manejo de la API
1. Pantalla principal del sistema, donde se encuentra el buscador y la lista de pokémones de 2 X 3
![image](https://github.com/Miguel-EMC/Api-Pokemon/assets/74844624/18d672dc-19f9-4d98-a37a-66be2eb97b0e)

2. En la parte inferior de la pantalla principal se encuentra una barra de paginación
![image](https://github.com/Miguel-EMC/Api-Pokemon/assets/74844624/6810d15a-0ff3-4da3-a746-e60446eab901)

3. Para realizar la busqueda se escribe en el input(nombre del pokémon) y se preciona el botón buscar
![image](https://github.com/Miguel-EMC/Api-Pokemon/assets/74844624/cff1bb03-24d7-4661-b59e-1505436bc364)
![image](https://github.com/Miguel-EMC/Api-Pokemon/assets/74844624/60a8469f-c011-4375-b97c-045ae43a90ab)

4. Para observar los detalles del pokémon se debe precionar a la tarjeta.
![image](https://github.com/Miguel-EMC/Api-Pokemon/assets/74844624/57ea8101-6acd-4791-9d33-c6b745fbfeec)

## Autor

- [Miguel Muzo](https://github.com/Miguel-EMC)

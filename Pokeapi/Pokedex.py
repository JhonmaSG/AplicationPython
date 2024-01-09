# interfaz
import flet as ft
# solucitudes a APi pokeapi
import requests
# Conjunto de librerias para conocer la 
# imagen de la consulta
import base64
from urllib.request import urlopen
from PIL import Image
from io import BytesIO
# tiempo de espera
import time
# Inicia el temporizador
import threading


def main(page):
    
    logo_pokedex = ft.Image(
        src=f"logo.png",
        width=350,
        height=170
    )

    # Configura el tamaño de la ventana
    page.window_width = 550       # window's width is 500 px
    page.window_height = 750      # window's height is 600 px
    page.update()

    # Alinea todos los controles en el centro
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    nombre = ft.TextField(label="Nombre", autofocus=True)
    submit = ft.ElevatedButton("Consultar")

    pokemon_image = ft.Image(
        src="backgroud.png",
        width=350,
        height=350
    )

    loading = ft.Text("Cargando...")
    loading.visible = False

    #Lógica de consulta a la API
    def btn_click(e):
        api_url_pokemon = f'https://pokeapi.co/api/v2/pokemon/{nombre.value}'
        result = requests.get(api_url_pokemon)

        # Muestra la animación de carga
        loading.visible = True
        page.update()

        # Tiempo de espera
        def delay():
            start_time = time.time()
            while time.time() - start_time < 0.25:
                pass
        
        # Ejecuta la función de retraso en un nuevo hilo
        threading.Thread(target=delay).start()

        if result.status_code == 200:
            pokemon_data = result.json()
            url_image = pokemon_data['sprites']['other']['official-artwork']['front_default']
            im = Image.open(urlopen(url_image)) #Se Accede a la imagen de la URL

            buffer = BytesIO()  #Almacenamos el buffer creado y convertir a base64
            im.save(buffer, format="png")
            image_base64 = base64.b64encode(buffer.getvalue()).decode()

            pokemon_image.src_base64 = image_base64
            pokemon_image.update()
        else:
            print("No se encontro el pokemon")
            # Muestra un mensaje de alerta
            def close_dlg(e):
                dlg.open = False
                page.update()

            dlg = ft.AlertDialog(
                content=ft.Text("No se encontró el Pokémon"),
                actions=[ft.TextButton("OK", on_click=lambda e: close_dlg(e))]
            )
            page.dialog = dlg
            dlg.open = True
            page.update()

        # Oculta el indicador de carga
        loading.visible = False
        page.update()
    
    column = ft.Column([
        submit,
        loading
    ])

    submit.on_click = btn_click
    page.add(
        logo_pokedex,
        nombre,
        column,
        pokemon_image
    ) 

ft.app(target=main)

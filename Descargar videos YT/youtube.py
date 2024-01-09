import flet as ft   #Flet = interfaz
from pytube import YouTube  #allow videos from Youtube
import os   #Manejar rutas en el Sis. Operativo

#Interfaz gráfica basica con Flet "Hola mundo Flet"
#def main(page):
#    pass
#

def main(page: ft.Page):

    page.title = "Mp3 and Mp4 Youtube"
    #page.vertical_alignment = "center"

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.YELLOW,
            primary_container=ft.colors.GREEN_200
        ),
    )

    lbl_texto = ft.Text(
        value = '1 link Mega 100% Real no FAKE Descargar MP3 y MP4 Youtube',
        size=30,
        color='yellow',
        weight='bold',
        italic=True
    )

    url = ft.TextField(label="Ingrese la URL", autofocus=True)
    submit1 = ft.ElevatedButton("Descargar Audio")
    submit2 = ft.ElevatedButton("Descargar Low HD")
    submit3 = ft.ElevatedButton("Descargar Full HD")

    def btn_click1(e):
        current_folder = os.getcwd()    #Ruta de Descarga
        yt = YouTube(url.value)
        video = yt.streams.get_audio_only()
        video.download(output_path=current_folder)

    submit1.on_click = btn_click1

    def btn_click2(e):
        current_folder = os.getcwd()    #Ruta de Descarga
        yt = YouTube(url.value)
        video = yt.streams.get_lowest_resolution()
        video.download(output_path=current_folder)

    submit2.on_click = btn_click2

    def btn_click3(e):
        current_folder = os.getcwd()    #Ruta de Descarga
        yt = YouTube(url.value)
        video = yt.streams.get_highest_resolution()
        video.download(output_path=current_folder)

    submit3.on_click = btn_click3
    page.add(lbl_texto,url,submit1, submit2, submit3)

ft.app(target=main)
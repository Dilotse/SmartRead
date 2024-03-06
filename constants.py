# =====Home view
import flet as ft
from flet import Image, Draggable, DragTarget, Text, DragTargetAcceptEvent, Container

image_width = 200
image_height = 200

image1 = ft.Image(
    src='source\Term1\week1\img001.png',
    width=image_width,
    height=image_height,
    fit=ft.ImageFit.CONTAIN, 
   
)

image2 = ft.Image(
    src='source\Term1\week1\img002.png',
    width=image_width,
    height=image_height,
    fit=ft.ImageFit.CONTAIN
)

image3 = ft.Image(
    src='source\Term1\week1\img003.png',
    width=image_width,
    height=image_height,
    fit=ft.ImageFit.CONTAIN
)

image4 = ft.Image(
    src='source\Term1\week1\img004.png',
    width=image_width,
    height=image_height,
    fit=ft.ImageFit.CONTAIN
)
image5 = ft.Image(
    src='source\Term1\week1\img005.png',
    width=image_width,
    height=image_height,
    fit=ft.ImageFit.CONTAIN
)

image6 = ft.Image(
    src='source\Term1\week1\img006.png',
    width=image_width,
    height=image_height,
    fit=ft.ImageFit.CONTAIN
)

words_data = [
    {"word": "Waking Up", "image": image1, "matched": False},
    {"word": "Brushing teeth", "image": image2, "matched": False},
    {"word": "Going to school", "image": image3, "matched": False},
    {"word": "Playing", "image": image4, "matched": False},
    {"word": "Eating dinner", "image": image5, "matched": False},
    {"word": "Sleeping", "image": image6, "matched": False}]

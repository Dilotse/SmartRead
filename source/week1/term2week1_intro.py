import functions as functions
from flet import MainAxisAlignment, CrossAxisAlignment, AppBar, Text, View
import flet as ft

def term2week1_intro(page: ft.Page):
    back_route = '../home'
    next_route = '/term2week1_intro_song'

    buttons = functions.create_buttons(page, back_route, next_route)
    text1 = functions.create_gradient_text('Introduce the theme: Friends',
                                     30, CrossAxisAlignment.START, [ft.colors.BLUE, ft.colors.RED])
    text2 = functions.create_gradient_text('Friends',
                                     30, CrossAxisAlignment.START, [ft.colors.BLUE, ft.colors.RED])
    return View(
        route='/term2week1_intro',
        controls=[
            AppBar(title=Text('Term 2: Friends: Week 1 - Introduce the theme'), bgcolor='purple'),
            text1, 
            text2, 
            ft.Image(src='source\Term1\week1\monday\Introduction_001.png', height=400, width=400),
            buttons
        ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=26
    )
from flet import *
import flet as ft
import functions as functions

view_name = '/slide13'


def slide13(page: ft.Page):
    back_route = '/term2week1_intro_song'
    next_route = '../home'
    buttons = functions13.create_buttons(page, back_route, next_route)
    page.padding = 0

    return View(
        route=view_name,
        controls=[Container(
            image_src='slide13.png',
            image_fit=ImageFit.SCALE_DOWN,
            expand=True,
            content=Control(),
            border=ft.border.all(2, ft.colors.RED))]
    )


if __name__ == '__main__':
    
    ft.app(target=slide13)

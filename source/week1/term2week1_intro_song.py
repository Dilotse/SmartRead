import functions as functions
from flet import *
import flet as ft

view_name = '/term2week1_intro_song'
def term2week1_intro_song(page: ft.Page):
    back_route = '/term2week1_intro'
    next_route = '/slide13'

    buttons = functions.create_buttons(page, back_route, next_route)
    text1 = functions.create_gradient_text('Song/Rhyme',
                                     30, CrossAxisAlignment.START, [ft.colors.BLUE, ft.colors.RED])
    text2 = functions.create_gradient_text('Song: “If you want to be a friend"',
                                     30, CrossAxisAlignment.START, [ft.colors.BLUE, ft.colors.RED])
    audio1Full= ft.Audio(src='source\sounds\Grade 1 Week 1\Song for the week\If you want to be a friend Grade 1 Week 1.mp3', autoplay=False)
    audio1Sep= ft.Audio(src='source\sounds\Grade 1 Week 1\Song for the week\1.SEPERATE If you want to be a friend clap your hands FIRST LINE.mp3')
    audio2Sep= ft.Audio(src='source\sounds\Grade 1 Week 1\Song for the week\2.SEPERATE If you want to be a friend clap your hands SECOND LINE.mp3')
    audio3Sep= ft.Audio(src='source\sounds\Grade 1 Week 1\Song for the week\3.SEPERATE A friend is someone who is always kind to you THIRD line.mp3')
    audio4Sep= ft.Audio(src='source\sounds\Grade 1 Week 1\Song for the week\4.SEPERATE if you want to be a friend clap your hands LAST line.mp3')

    return View(
        route=view_name,
        controls=[
            AppBar(title=Text('Friends:  Week 1 Monday Daily Activities - 15 Minutes'), bgcolor='green'),
            text1, 
            text2, 
            buttons,
            Column(controls=[ft.ElevatedButton(text='Play whole song',icon='PLAY_ARROW_ROUNDED', height=200, width=200,bgcolor="green", on_click=lambda _: audio1Full.play()), 
                    ft.ElevatedButton(text='If you want to be a friend, clap your hands',icon='CHECK_BOX_OUTLINE_BLANK', height=100, width=200,bgcolor="blue", on_click=lambda _: audio1Sep.play()),
                    ft.ElevatedButton(text='If you want to be a friend, clap your hands',icon='CHECK_BOX_OUTLINE_BLANK', height=100, width=200,bgcolor="yellow", on_click=lambda _: audio2Sep.play()),
                    ft.ElevatedButton(text='A friend is someone who is always kind to you',icon='CHECK_BOX_OUTLINE_BLANK', height=100, width=200,bgcolor="red", on_click=lambda _: audio3Sep.play()),
                    ft.ElevatedButton(text='If you want to be a friend, clap your hands',icon='CHECK_BOX_OUTLINE_BLANK', height=100, width=200,bgcolor="orange", on_click=lambda _: audio4Sep.play())], 
                    alignment=MainAxisAlignment.CENTER)
        ],
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=26,
            auto_scroll=True

    )
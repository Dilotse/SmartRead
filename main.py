import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text, Row, Column
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
from flet import Text, LinearGradient, ShaderMask, CrossAxisAlignment
import constants as constants
import functions as functions

from source.week1.term2week1_intro import term2week1_intro
from source.week1.term2week1_intro_song import term2week1_intro_song
from source.Term1.week1.monday import slide13


def main(page: ft.Page):
    page.title = 'Flet Application'
    page.fonts = {'Teacher Pet': 'source\Fonts\TeachersPet.TTF'}

    def create_buttons(page, back_route: str, next_route: str):
      # Create buttons with click handlers
        back_button = ElevatedButton(
            text="Back", on_click=lambda _: page.go(back_route))
        next_button = ElevatedButton(
            text="Next", on_click=lambda _: page.go(next_route))

        # Create Rows with specific alignment for each button
        back_row = Row(alignment=MainAxisAlignment.START,
                       controls=[back_button])
        next_row = Row(alignment=MainAxisAlignment.END, controls=[next_button])

        # Combine the rows into a single column
        button_column = Column(controls=[back_row, next_row])

        return button_column

    def create_gradient_text(
        text: str,
        size: int = 30,
        alignment: CrossAxisAlignment = CrossAxisAlignment.CENTER,
        gradient_colors: list[ft.colors] = [
            ft.colors.YELLOW, ft.colors.ORANGE
        ],
        gradient_stops: list[float] = [0.0, 1.0],
    ):
        """
        Creates a Text widget with a background gradient and optional alignment.

        Args:
            text (str): The text to display.
            size (int): The font size for the text.
            alignment (CrossAxisAlignment, optional): The alignment of the text within the widget. Defaults to CrossAxisAlignment.CENTER.
            gradient_colors (list[Colors], optional): The list of colors to use in the gradient. Defaults to [Colors.YELLOW, Colors.ORANGE].
            gradient_stops (list[float], optional): The list of positions for the colors in the gradient. Defaults to [0.0, 1.0].

        Returns:
            Text: The Text widget with the gradient background.
        """

        gradient = ft.LinearGradient(  # Use ft.LinearGradient directly
            colors=gradient_colors, stops=gradient_stops
        )
        return ShaderMask(
            content=Text(
                value=text,
                size=size,
                color=ft.colors.WHITE,
                text_align=ft.TextAlign.CENTER,
            ),
            blend_mode=ft.BlendMode.SRC_IN,
            shader=gradient
        )

    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        # Define next and back page routes
        back_route = '/third_page'
        next_route = '/term2week1_intro'

        # Use the create_buttons function with specific routes
        buttons = create_buttons(page, back_route, next_route)
        text1 = create_gradient_text('Extension Activities (Independent work/Assessments for learners)',
                                     30, CrossAxisAlignment.START, [ft.colors.BLUE, ft.colors.RED])
        text2 = create_gradient_text('Activity 1 - DBE Workbook 1: Let’s talk, page 50',
                                     30, CrossAxisAlignment.START, [ft.colors.BLUE, ft.colors.RED])
        text3 = create_gradient_text('Day and Night',
                                     30, CrossAxisAlignment.START, [ft.colors.BLUE, ft.colors.RED])
        text4 = create_gradient_text('Look at these pictures and match what the children are doing',
                                     30, CrossAxisAlignment.START, [ft.colors.BLUE, ft.colors.RED])

        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text('Home'), bgcolor='blue'),
                    text1,
                    text2,
                    text3,
                    text4,
                    buttons,
                    Column([functions.create_draggable_word(item['word'])
                           for item in constants.words_data]),
                    Row(controls=[
                        functions.create_image_drop_target(
                            page, constants.image1),
                        functions.create_image_drop_target(
                            page, constants.image2),
                        functions.create_image_drop_target(
                            page, constants.image3),
                        functions.create_image_drop_target(
                            page, constants.image4),
                        functions.create_image_drop_target(
                            page, constants.image5),
                        functions.create_image_drop_target(
                            page, constants.image6)],

                        alignment=MainAxisAlignment.CENTER,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                        spacing=20)
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=10
            )
        )

        # =====term2week1_intro
        if page.route == '/term2week1_intro':
            page.views.append(term2week1_intro(page))

        # =====term2week1_intro_song
        if page.route == '/term2week1_intro_song':
            page.views.append(term2week1_intro_song(page))
        
        # if page.route == '/slide13':
        #     page.views.append(slide13(page))

        page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main)

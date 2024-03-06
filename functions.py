import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text, Row, Column
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
from flet import Text, LinearGradient, ShaderMask, CrossAxisAlignment
from flet import Image, Draggable, DragTarget, Text, DragTargetAcceptEvent, Container
import constants as constants


def on_accept(e: DragTargetAcceptEvent):
    dragged_word = e.data  # Get the text of the dragged word
    target_image = e.control.content  # Get the Image widget associated with the target

    if dragged_word == "Correct Label for Image":  # Replace with the actual matching condition
        # Success!
        e.control.content = Container(
            bgcolor=ft.colors.GREEN,
            content=target_image  # Keep the image in the target
        )
    else:
        # Failure
        e.control.content = Container(
            bgcolor=ft.colors.RED,
            content=target_image  # Keep the image in the target
        )


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

# =====Drag Functions=====


def create_draggable_word(word):
    return ft.Draggable(
        content=ft.Text(word, color=ft.colors.YELLOW_500),
        group="words",  # A group for drag-and-drop
        data=word  # Store the word itself for matching
    )


def create_image_drop_target(page, image_control):
    return ft.DragTarget(
        group="words",  # Same group as the draggable words
        content=image_control,
        on_accept=lambda e: word_dropped(page, e, image_control),
    )


def word_dropped(page, e: ft.DragTargetAcceptEvent, image_control):
    word = e.data
    # Find matching data item based on the image_control (implement matching logic)
    matching_data = next(
        (item for item in constants.words_data if item["image"] == image_control), None)

    if matching_data and word == matching_data["word"]:
        matching_data["matched"] = True
        # Do something to visually indicate success (e.g., disable word, change color, etc.)
        print("Correct match!")

        # Check if all words are matched
        if all(item["matched"] for item in constants.words_data):
            print("All words matched!")
            # Celebrate or move to the next activity
    else:
        print("Try again!")  # Optional feedback for incorrect placement

def items(text):
        items = []
        items.append(
            ft.Container(
                content=ft.Text(value=str(text),
                    alignment=ft.alignment.center,
                    width=500,
                    height=500,
                    bgcolor=ft.colors.AMBER_500,
                    )
            )  
        )     
        return items

def column_with_horiz_alignment(align: ft.CrossAxisAlignment):
        return ft.Column(
            [
                ft.Text(str(align), size=16),
                ft.Container(
                    content=ft.Column(
                        items(3),
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=align,
                    ),
                    bgcolor=ft.colors.AMBER_100,
                    width=100,
                ),
            ]
        )

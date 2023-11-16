from typing import Any, List, Optional, Tuple, Union
from flet import *
from flet_core.alignment import Alignment
from flet_core.blur import Blur
from flet_core.border import Border
from flet_core.control import Control, OptionalNumber
from flet_core.form_field_control import InputBorder
from flet_core.gradients import Gradient
from flet_core.ref import Ref
from flet_core.shadow import BoxShadow
from flet_core.text_style import TextStyle
from flet_core.textfield import KeyboardType, TextCapitalization
from flet_core.theme import Theme
from flet_core.types import AnimationValue, BlendMode, BorderRadiusValue, BoxShape, ClipBehavior, CrossAxisAlignment, ImageFit, ImageRepeat, MainAxisAlignment, MarginValue, OffsetValue, PaddingValue, ResponsiveNumber, RotateValue, ScaleValue, ScrollMode, TextAlign, ThemeMode
from controls import nav_bar, postControl
from view import ShowMenu, ChangeRout
import openai
import time


openai.api_key = "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"


def main_sytle() -> dict:
    return {
        "width": 700,
        "height": 500,
        "bgcolor": "#1d1d1d",
        "border_radius": 10,
        "padding": 15,
        "expand": True,

    }


def prompt_style() -> dict:
    return {
        "width": 700,
        "height": 40,
        "bgcolor": "#f0f3f6",
        "content_padding": 10,
        "border_color": "transparent",
        "cursor_color": "black",
        "color": "black",
    }


class MainContentArea(Container):
    def __init__(self):
        super().__init__(**main_sytle())
        self.chat = ListView(
            expand=True,
            height=200,
            spacing=15,
            auto_scroll=True,

        )
        self.content = self.chat


class CreateMessage(Column):
    def __init__(self, name: str, message: str) -> None:
        self.name = name
        self.message = message
        self.text = Text(self.message)
        super().__init__(spacing=4)
        self .controls = [Text(self.name, opacity=0.6), self.text]


class Prompt(TextField):
    def __init__(self, chat: ListView) -> None:
        super().__init__(**prompt_style(), on_submit=self.run_prompt)
        self.chat: ListView = chat

    def animate_text_output(self, name: str, prompt: str) -> None:
        word_list: list = []
        msg = CreateMessage(name, "")
        self.chat.controls.append(msg)

        for word in list(prompt):
            word_list.append(word)
            msg.text.value = "".join(word_list)
            self.chat.update()
            time.sleep(0.008)

    def user_output(self, prompt):
        self.animate_text_output(name="Me", prompt=prompt)

    def gpt_output(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            message=[{"role": "user", "content": prompt}]
        )
        response = response.choices[0].message.content.srip()
        self.animate_text_output(name="MedBot", prompt=response)

    def run_prompt(self, event) -> None:
        # print(event.control.value)
        text: Any = event.control.value

        self.value = ""
        self.update()

        self.user_output(prompt=text)
        self.gpt_output(prompt=text)


def _view_(first_name: str, last_name: str):
    ChatArea = MainContentArea()
    Text_bar = Prompt(chat=ChatArea.chat)
    return View(
        "/index", bgcolor="white54",
        controls=[
            Column(
                expand=True,
                controls=[
                    Row(
                        expand=True,
                        controls=[
                            Column(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Container(
                                        margin=-10,
                                        bgcolor="#1d1d1d",
                                        width=60,
                                        expand=True,
                                        animate=animation.Animation(
                                            350, "decelerate"),
                                        on_hover=lambda e: ShowMenu(e),
                                        content=nav_bar.ModerNavBar(
                                            # pas the funcions
                                            lambda e: ChangeRout(e, "/login"),
                                            lambda e: ChangeRout(
                                                e, "/profile"),
                                            lambda e: ChangeRout(e, "/index"),
                                        ),
                                    )
                                ]
                            ),
                            VerticalDivider(width=10, color="transparent"),
                            Column(
                                expand=True,
                                alignment=MainAxisAlignment.START,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                controls=[
                                    Text(
                                        "Medbot",
                                        size=26,
                                        color="black",
                                        weight="w600"
                                    ),
                                    Divider(height=30, color="transparent"),
                                    ChatArea,
                                    Divider(height=5, color="transparent"),
                                    Text_bar,
                                    Divider(height=5, color="transparent"),
                                    # postControl.PostControl(),
                                    # Change 'black' for 'transparent'
                                    # Divider(height=30, color="black"),

                                    # Column(expand=True, scroll="hidden"),
                                ]
                            ),
                        ]
                    )
                ]
            )
        ]
    )

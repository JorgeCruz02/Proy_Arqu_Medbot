from typing import Any, List, Optional, Union
from flet import *
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue
import view

class PostControl(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return Container(
            bgcolor="#f0f3f6",
            width=500,
            height=52,
            border_radius=6,
            padding=5,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Container(
                        alignment=alignment.center,
                        content=TextField(
                            content_padding=10,
                            height=42,
                            width=320,
                            text_size=12,
                            color="black",
                            border_radius=6,
                            bgcolor="#f0f3f6",
                            border_color="transparent",
                            filled=True,
                            cursor_color="black",
                            cursor_width=1,
                            hint_text="Start writing somthing here ....",
                            hint_style=TextStyle(
                                size=11,
                                color="black",
                            )
                        )
                    ),
                    Container(
                        content=ElevatedButton(
                            #on_click=self.func,
                            content=Text(
                                "Post",
                                size=11,
                                weight="blod",
                            ),
                            style=ButtonStyle(
                                shape={
                                    "": RoundedRectangleBorder(radius=8),
                                },
                                color={
                                    "": "white",
                                },
                            ),
                            height=42,
                            width=100,
                        )
                    )
                ]
            )
        )
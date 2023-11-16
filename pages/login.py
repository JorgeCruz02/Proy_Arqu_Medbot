from flet import *

# Import Controls
from controls import inputText

from view import ChangeRout, LogInUser
#


def _view_():
    return View(
        "/login",
        bgcolor="#2E4053",
        horizontal_alignment=CrossAxisAlignment.CENTER,
        vertical_alignment=CrossAxisAlignment.CENTER,
        controls=[
            Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        width=350,
                        height=500,
                        border_radius=8,
                        bgcolor="#34495E",
                        border=border.all(3, "#dbdbdb"),
                        alignment=alignment.center,
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Divider(height=20, color="transparent"),
                                Text(
                                    "Login",
                                    size=26,
                                    color="white",
                                    weight="w600"
                                ),
                                Text(
                                    "Use the from below to log into your account.",
                                    size=12,
                                    color="white",
                                    weight="w400"
                                ),
                                Divider(height=40, color="transparent"),
                                Column(
                                    spacing=5,
                                    controls=[
                                        inputText.InputTextField(
                                            "Email", False),
                                        inputText.InputTextField(
                                            "Password", True),
                                    ],
                                ),
                                Row(
                                    width=300,
                                    alignment=MainAxisAlignment.END,
                                    controls=[
                                        Text(
                                            "Forgot Password?",
                                            color="white",
                                            weight="bold",
                                            size=10,
                                        )
                                    ],
                                ),
                                Divider(height=5, color="transparent"),
                                # another control
                                inputText.SingInOption(
                                    "Log In", lambda e: LogInUser(e)),
                                Divider(height=60, color="transparent"),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=4,
                                    controls=[
                                        Text(
                                            "Don`t have an account?",
                                            color="white",
                                            size=10,
                                            weight="bold",
                                        ),
                                        Container(
                                            on_click=lambda e: ChangeRout(
                                                e, "/register"),
                                            content=Text(
                                                "Sing in",
                                                color="red900",
                                                size=10,
                                                weight="bold",
                                            ),
                                        )
                                    ],
                                ),
                            ],
                        ),
                    ),
                    # footer UI
                    Column(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            Divider(height=60, color="transparent"),
                            # another control
                            inputText.GetFooter(),
                            Row(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Text(
                                        "© 2023 Line Indent",
                                        size=10,
                                        weight="w500",
                                        color="white",
                                    )
                                ]
                            )
                        ]
                    ),
                ]
            )
        ]
    )

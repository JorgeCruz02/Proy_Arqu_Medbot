from flet import *


class ProfileData(UserControl):
    def __init__(self, cerated_on, last_login, first_name, last_name, email):
        self.created_on = cerated_on
        self.last_login = last_login
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        super().__init__()

    def ReturnText(self, name, size):
        return Text(
            value=name,
            size=size,
            color="black",
            weight="blod",
        )

    def build(self):
        return Column(
            controls=[
                Divider(height=30, color="transparent"),
                Row(
                    controls=[
                        Text(
                            "user profile Information",
                            size=25,
                            color="black",
                            weight="blod",
                        )
                    ]
                ),
                Divider(height=10, color="black",),
                Divider(height=20, color="transparent"),

                Container(
                    width=400,
                    content=Row(
                        alignment=MainAxisAlignment.START,
                        spacing=40,
                        controls=[
                            Column(
                                spacing=2,
                                controls=[
                                    self.ReturnText("User Created On", 10),
                                    self.ReturnText(self.created_on, 12),
                                ],
                            ),
                            Column(
                                spacing=2,
                                controls=[
                                    self.ReturnText("Last Login", 10),
                                    self.ReturnText(self.last_login, 12),
                                ]
                            )
                        ]
                    )
                ),
                Divider(height=20, color="transparent"),
                Container(
                    width=400,
                    content=Row(
                        alignment=MainAxisAlignment.START,
                        spacing=40,
                        controls=[
                            Column(
                                spacing=2,
                                controls=[
                                    self.ReturnText("First Name", 10),
                                    self.ReturnText(self.first_name, 12),
                                ],
                            ),
                            Column(
                                spacing=2,
                                controls=[
                                    self.ReturnText("Last Name", 10),
                                    self.ReturnText(self.last_name, 12),
                                ]
                            )
                        ]
                    )
                ),

                Divider(height=20, color="transparent"),
                Container(
                    width=400,
                    content=Row(
                        alignment=MainAxisAlignment.START,
                        spacing=40,
                        controls=[
                            Column(
                                spacing=2,
                                controls=[
                                    self.ReturnText("Email", 10),
                                    self.ReturnText(self.email, 12),
                                ],
                            ),
                        ]
                    )
                ),
            ],
        )

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
            color="white",
            weight="blod",
        )

    def build(self):
        return Column(
            controls=[
                Divider(height=30, color="transparent"),
                Row(
                    controls=[
                        Text(
                            "Información del Usuario",
                            size=25,
                            color="white",
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
                                    self.ReturnText("Usuario creado en:", 18),
                                    self.ReturnText(self.created_on, 12),
                                ],
                            ),
                            Column(
                                spacing=2,
                                controls=[
                                    self.ReturnText("Último Login:", 18),
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
                                    self.ReturnText("Nombre:", 18),
                                    self.ReturnText(self.first_name, 12),
                                ],
                            ),
                            Column(
                                spacing=2,
                                controls=[
                                    self.ReturnText("Apellidos:", 18),
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
                                    self.ReturnText("Email:", 18),
                                    self.ReturnText(self.email, 12),
                                ],
                            ),
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
                                    self.ReturnText("Historial Medico:", 18),
                                    
                                ],
                            ),
                        ]
                    )
                ),
            ],
        )

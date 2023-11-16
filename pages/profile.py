from flet import *
from controls import nav_bar, profile_data
from view import ShowMenu, ChangeRout
# , LogOutUser


def _view_(crated_on, last_login, first_name, last_name, email):
    return View(
        "/profile",
        bgcolor="34495E",
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
                                        bgcolor="#1B2631",
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
                            VerticalDivider(width=60, color='Transparent'),
                            profile_data.ProfileData(
                                crated_on, last_login, first_name, last_name, email),
                        ]
                    )
                ]
            )
        ]
    )

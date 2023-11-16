# In this page is where input from the user comes first.
import pyrebase

from main import _modul_List
from datetime import datetime

Config = {
    "apiKey": "AIzaSyA9L9bvYY5K5tqX4Lt29mG1vt22ci8yB7Q",
    "authDomain": "medot-flet-firebase.firebaseapp.com",
    "projectId": "medot-flet-firebase",
    "storageBucket": "medot-flet-firebase.appspot.com",
    "messagingSenderId": "431755771996",
    "appId": "1:431755771996:web:186dae4d32282ca6b82699",
    # Esta se  encuentra en el apartado de 'Realtime Database' en 'firebase'
    "databaseURL": "https://medot-flet-firebase-default-rtdb.firebaseio.com/",
}


# store information
global SESSION
SESSION = {}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()

#


def ChangeRout(e, page_route):
    global _modul_List
    print(e)
    # cuando llamamos a la funcion primero deseamos limpiar 'views list'
    e.page.views.clear()

    if page_route == '/register':
        e.page.views.append(
            #
            _modul_List[page_route].loader.load_module()._view_()
        )
        e.page.go("/register")

    if page_route == "/login":
        e.page.views.append(
            #
            _modul_List[page_route].loader.load_module()._view_()
        )
        e.page.go("/login")
        # e.page.go("/register")

    if page_route == "/index":
        e.page.views.append(
            _modul_List[page_route].loader.load_module()._view_(
                SESSION["firstName"], SESSION["lastName"],
            )
        )
        # DisplayTask(e)
        e.page.go("/index")

    if page_route == "/profile":
        create_on, last_login, first_name, last_name, email = ProfileUserData()
        e.page.views.append(
            _modul_List[page_route].loader.load_module()._view_(
                create_on, last_login, first_name, last_name, email
            )
        )
        e.page.go("/profile")
    else:
        pass

    e.page.update()


def ProfileUserData():
    global _modul_List
    #print("session:")
    #print(SESSION)
    user_info = []
    info = auth.get_account_info(SESSION["users"]["idToken"])
    data = ["createdAt", "lastLoginAt"]
    for key in info:
        if key == "users":
            for item in data:
                user_info.append(
                    datetime.fromtimestamp(int(info[key][0][item])/1000).strftime(
                        "%D - %H:%M %p"
                    )
                )
    user_info.append(SESSION["firstName"])
    user_info.append(SESSION["lastName"])
    user_info.append(SESSION["users"]["email"])
    
    #print(user_info)
    return user_info


def RegisterUser(e):
    for page in e.page.views[:]:
        if page.route == "/register":
            res = page.controls[0].controls[0].content.controls[4]
            try:

                auth.create_user_with_email_and_password(
                    res.controls[2].content.value,
                    res.controls[3].content.value,
                )

                #
                data = {
                    "firstName": res.controls[0].content.value,
                    "lastName": res.controls[1].content.value,
                    "email": res.controls[2].content.value,
                    "password": res.controls[3].content.value,
                }

                # note: before writhing to the DB, you need to change the privacy rules
                db.child('users').push(data)

                e.page.views.clear()
                e.page.views.append(
                    _modul_List["/login"].loader.load_module()._view_())
                e.page.update()

            except Exception as e:
                pass
            finally:
                for item in res.controls[:]:
                    item.content.value = None
                    item.content.update()


#
def LogInUser(e):
    first_name, last_name = GetUserDetail(e)

    #print(first_name, last_name)
    if first_name == "erro":
        e.page.views.clear()
        e.page.views.append(
            _modul_List["/login"].loader.load_module()._view_()
        )
        e.page.go("/login")
        e.page.update()
    else:
        e.page.views.clear()
        e.page.views.append(
            _modul_List["/index"].loader.load_module()._view_(first_name, last_name))
        e.page.go('/index')
        e.page.update()


def GetUserDetail(e):
    global _modul_List
    for page in e.page.views[:]:
        if page.route == "/login":
            res = page.controls[0].controls[0].content.controls[4]
            try:
                user = auth.sign_in_with_email_and_password(
                    res.controls[0].content.value,
                    res.controls[1].content.value,
                )

                SESSION["users"] = user
                #print(user)

                val = db.child("users").get()
                for i in val:
                    # here check the database email with email user is trying
                    if i.val()["email"] == user["email"]:
                        first_name = i.val()["firstName"]
                        last_name = i.val()["lastName"]
                        SESSION["path"] = i.key()
                        SESSION["firstName"] = first_name
                        SESSION["lastName"] = last_name

                    return [first_name, last_name]

            except Exception as e:
                return ["erro", "fallo"]


def GetUserDetailPrueba(rout):
    if rout == "/login":
        res = ["ppython@gmail.com","pass0000"]
        try:
            user = auth.sign_in_with_email_and_password(
                res[0],
                res[1],
            )
    
            SESSION["users"] = user
            #print(user)

            val = db.child("users").get()
            for i in val:
                # here check the database email with email user is trying
                if i.val()["email"] == user["email"]:
                    first_name = i.val()["firstName"]
                    last_name = i.val()["lastName"]
                    SESSION["path"] = i.key()
                    SESSION["firstName"] = first_name
                    SESSION["lastName"] = last_name

                return [first_name, last_name]

        except Exception as e:
            return ["erro", "fallo"]


# toggle menu


def ShowMenu(e):
    for page in e.page.views[:]:
        if page.route == "/index" or page.route == "/profile":
            if e.data == 'true':
                page.controls[0].controls[0].controls[0].controls[0].width = 185
                page.update()
            else:
                page.controls[0].controls[0].controls[0].controls[0].width = 60
                page.update()

# importa librerias
import flet
import os
import importlib.util

# Importar las vistas
global _mobule_List
_modul_List = {}


for _, dirs, _ in os.walk(r'./'):

    for dir in dirs:
        if dir == 'pages':
            for filename in os.listdir(dir):

                _file = os.path.join(dir, filename)

                #
                if os.path.isfile(_file):
                    filename = filename[:-3]

                    _modul_List[
                        "/" + filename
                    ] = importlib.util.spec_from_file_location(filename, _file)


def main(page: flet.Page):
    page.title = 'Flet Web'

    # Mientras se hacia la UI esta linea es modificable
    page.views.append(_modul_List["/login"].loader.load_module()._view_(
       #"Test", "index"
       #"Test","Profile","afdsa","afdsa","afdsa",
    ))

    page.go("/login")
    page.update()
    pass


if __name__ == '__main__':
    flet.app(target=main)

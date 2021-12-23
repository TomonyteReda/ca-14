from modules.kursas import Kursas


class PythonKursas(Kursas):

    def __init__(self, destytojas, trukme, pavadinimas='python'):
        super().__init__(destytojas, trukme, pavadinimas)

    def destyti(self):
        print('Vyksta programavimas!')

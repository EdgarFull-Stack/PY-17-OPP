# Task 3
class Darbuotojas:
    def __init__(self, vardas, pavarde, asmens_kodas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.__atlyginimas = None
        self.__asmens_kodas = asmens_kodas

    @property
    def lytis(self):
        return 'Vyras' if str(self.__asmens_kodas)[0] == '3' else 'Moteris'

    @property
    def atlyginimas(self):
        if self.__atlyginimas >= 500:
            return self.__atlyginimas if self.__atlyginimas else 0
        else:
            return('atlyginimas negali būti mažesnis nei minimalus')

    @atlyginimas.setter
    def atlyginimas(self, suma):
        self.__atlyginimas = suma if suma >= 500 else 1

    @property
    def mokesciai(self):
        if self.__atlyginimas>=500:
            return self.__atlyginimas*0.8
        else:
            return 'atlyginimas negali būti mažesnis nei minimalus'

darb1 = Darbuotojas('Edgar', 'Lip',30202020202,)
darb1.atlyginimas = 700
atl2 = darb1.atlyginimas
print(f'Atlyginimas: {atl2}')
print(darb1.lytis)
atlmk = darb1.mokesciai
print(f'Po mokesciu: {atlmk}')


# Example
class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos, asmens_kodas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos
        self.__atlyginimas = None
        self.__asmens_kodas = asmens_kodas


    @property
    def lytis(self):
        return 'Vyras' if str(self.__asmens_kodas)[0] == '3' else 'Moteris'
    @property
    def atlyginimas(self):
        return self.__atlyginimas if self.__atlyginimas else 0

    @atlyginimas.setter
    def atlyginimas(self, suma):
        self.__atlyginimas = suma if suma >= 0 else 1

darb1 = Darbuotojas('Edgar', 'Lip','Vadovas', 399999999)
atl = darb1.atlyginimas
print(atl)
darb1.atlyginimas = 5000
atl2 = darb1.atlyginimas
print(atl2)
print(darb1.lytis)

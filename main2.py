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
print('-'*40)
# Example
class Calculator:
    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def sub(num1, num2):
        return num1 - num2
a = Calculator.add(1,2)
print(a)
a = Calculator.sub(2,1)
print(a)
print('-'*40)
# Example
class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos

    @classmethod
    def sukurt_is_vienos_eilutes(cls, eilute):
        vardas, pavarde, pareigos = eilute.split()
        return cls(vardas, pavarde, pareigos)

    def __str__(self):
        return f'{self.vardas} {self.pavarde} Pareigos: {self.pareigos}'

    def pakeisti_pareigas(self, naujos_pareigos):
        self.pareigos = naujos_pareigos


eilute = 'Edgar Edgar Developer'
darbuotojas = Darbuotojas.sukurt_is_vienos_eilutes(eilute)
print(darbuotojas)

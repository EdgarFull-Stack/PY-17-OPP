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
            return 'atlyginimas negali būti mažesnis nei minimalus'

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
#  Task 4
class Matematika:
    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def minus(num1, num2):
        return num1 - num2

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        return num1 / num2

    @staticmethod
    def ar_lyginis(num3):
        return num3 % 2 ==0
a = Matematika.add(1,2)
print(a)
a = Matematika.minus(2,1)
print(a)
a = Matematika.multiply(2,2)
print(a)
a = Matematika.divide(6,2)
print(a)
a = Matematika.ar_lyginis(7)
print(a)
print('-'*40)
# Task 5
class Automobilis:
    def __init__(self, marke, modelis, metai):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai

    @classmethod
    def sukurti_is_string(cls, eilute):
        marke, modelis, metai = eilute.split()
        return cls(marke, modelis, metai)

    def __str__(self):
        return f'{self.marke} {self.modelis} {self.metai}'

    @classmethod
    def naujausias_modelis(cls, automobiliai):
        return max(automobiliai, key=lambda listas: listas.metai)

auto1 = Automobilis.sukurti_is_string('BMW XM 2024')
auto2 = Automobilis.sukurti_is_string('Audi RS6 2025')
auto3 = Automobilis.sukurti_is_string('Mercedes S63 2023')
automobiliai = [auto1, auto2, auto3]

print(auto1)
print(auto2)
print(auto3)
naujausias = Automobilis.naujausias_modelis(automobiliai)
print(f'Naujausias: {naujausias}')





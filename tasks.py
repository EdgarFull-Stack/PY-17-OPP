# Task 1
class Studentas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        self._pazymiai = []

    def prideti_pazymi(self, pazymys):
        if 1 <= pazymys <= 10:
            self._pazymiai.append(pazymys)
        else: print('Prideti galima tik pazymi nuo 1 iki 10')

    def rodyti_vidurki(self):
        if self._pazymiai:
            return (sum(self._pazymiai) / len(self._pazymiai))
        else:
            print('Nera pazymiu')

# Additional
class StudentasLyderis(Studentas):
    def __init__(self, vardas, pavarde):
        super().__init__(vardas, pavarde)
        self.bonus_taskai = 0

    def prideti_bonus_taskus(self, taskai):
        if taskai > 0:
            self.bonus_taskai += taskai
        else:
            print('Iveskite teigiama skaiciu')

    def rodyti_vidurki(self):
        vidurkis = super().rodyti_vidurki()
        if vidurkis:
            return vidurkis + self.bonus_taskai


studentas = Studentas('Edgar', 'Fasttrack')
studentas.prideti_pazymi(5)
studentas.prideti_pazymi(7)
studentas.prideti_pazymi(8)
print(studentas.rodyti_vidurki())
print('-'*20)
lyderis = StudentasLyderis('Edgaras','Lip')
lyderis.prideti_pazymi(9)
lyderis.prideti_pazymi(7)
lyderis.prideti_bonus_taskus(2)
print(f'Lyderio vidurkis {lyderis.rodyti_vidurki()}')
print('-'*40)
# Task 2
class BankoSaskaita:
    def __init__(self, savininkas):
        self.savininkas = savininkas
        self.__balansas = 0

    def gauti_balansa(self):
        print(f'Balansas yra: {self.__balansas} ')

    def prideti_pinigus(self, suma):
        if suma > 0:
            self.__balansas += suma
            print(f'{suma} prideta prie balanso')
        else:
            print('Iveskite teigiama skaiciu')

    def nuskaičiuoti_pinigus(self, suma):
        if suma > 0:
            if self.__balansas >= suma:
                self.__balansas -= suma
                print(f'{suma} nuskaiciuota nuo balanso ')
            else:
                print('Nepakanka balanso')
        else:
            print('Iveskite teigiama nurasymo skaiciu')

saskaita = BankoSaskaita('Edgar')

print(saskaita.gauti_balansa())
saskaita.prideti_pinigus(50)
print(saskaita.gauti_balansa())
# pavyzdys kad nepasiekiama
# print(saskaita.__balansas)
saskaita.nuskaičiuoti_pinigus(30)
print(saskaita.gauti_balansa())
saskaita.nuskaičiuoti_pinigus(30)
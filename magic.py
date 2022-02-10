color = ["black", "white", "grey"]
position = [1, 2, 3, 4]

Tahoe = {
    'name': 'Tahoe',
    'type': 'kupe',
    'color': color[0:1],
    'position': position,
}

Nexia = {
    'name': 'Nexia',
    'type': 'sedan',
    'color': color,
    'position': position[1:3],
}

Captiva = {
    'name': 'Captiva',
    'type': 'sedan',
    'color': color,
    'position': position,
}

Malibu = {
    'name': 'Malibu',
    'type': 'kupe',
    'color': color,
    'position': position,
}

Cobalt = {
    'name': 'Cobalt',
    'type': 'sedan',
    'color': color,
    'position': position,
}


class Gmmotors:
    def __init__(self):
        self.gm_car_sedan = [Nexia, Cobalt]
        self.gm_car_kupe = [Malibu]
        self.gm_car_SUV = [Tahoe]
        self.gm_car_crossover = [Captiva]
        self.index01 = 1
        self.index02 = 1
        self.index03 = 1


class Sedan(Gmmotors):
    def sedan(self):
        x = 0
        for c in self.gm_car_sedan:
            print(str(x) + ' ' + c['name'])
            x += 1
        self.index01 = int(input('Нажмите на цифру что бы выбрать машину: '))
        Sedan_auto.collor_sedan()

    def collor_sedan(self):
        x = 0
        for i in self.gm_car_sedan[self.index01]["color"]:
            print(str(x) + ' ' + i)
            x += 1
        self.index02 = int(input('Отлично, теперь выберите цвет: '))
        Sedan_auto.position_sedan()

    def position_sedan(self):
        x = 0
        for z in self.gm_car_sedan[self.index01]["position"]:
            print(str(x) + '. ' + str(z) + ' позиция')
            x += 1
        self.index03 = int(input('Превосходно, теперь выберите позицию: '))

        print(f"""
        Вы приобрели машину типа "SEDAN" {self.gm_car_sedan[self.index01]['name']}
        Цвета {self.gm_car_sedan[self.index01]['color'][self.index02]}
        Позиции № {self.gm_car_sedan[self.index01]['position'][self.index03]}
        """)


class Kupe(Gmmotors):
    def kupe(self):
        x = 0
        for c in self.gm_car_kupe:
            print(str(x) + ' ' + c['name'])
            x += 1
        self.index01 = int(input('Выберите машину: '))

    def collor_kupe(self):
        x = 0
        for i in self.gm_car_kupe[self.index01]["color"]:
            print(str(x) + ' ' + i)
            x += 1
        self.index02 = int(input('Отлично, теперь выберите цвет: '))

    def position_kupe(self):
        x = 0
        for z in self.gm_car_kupe[self.index01]["position"]:
            print(str(x) + '. ' + str(z) + ' позиция')
            x += 1
        self.index03 = int(input('Превосходно, теперь выберите позицию: '))

        print(f"""
             Вы приобрели машину типа "SEDAN" {self.gm_car_kupe[self.index01]['name']}
             Цвета {self.gm_car_kupe[self.index01]['color'][self.index02]}
             Позиции № {self.gm_car_kupe[self.index01]['position'][self.index03]}
             """)


Sedan_auto = Sedan()
Kupe_auto = Kupe()
while True:
    print("""Здраствуйте, добро пожаловать в GM MOTORS.
    1.Седан |  2.Kupe  |  3.Внедорожник  |  4.Кроссовер""")

    client_chose = int(input('Выберите пожалуйста type машины которую хотите приобрести: '))
    if client_chose == 1:
        Sedan_auto.sedan()
    elif client_chose == 2:
        Kupe_auto.kupe()

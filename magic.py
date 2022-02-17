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
        self.client_chose01 = 1
        self.client_chose02 = 1
        self.client_chose03 = 1


class Sedan(Gmmotors):
    def sedan(self):
        type_sedan = self.gm_car_sedan
        for i, item in enumerate(type_sedan):
            print(i + 1, item['name'])
        try:
            self.client_chose01 = int(input('Нажмите на цифру что бы выбрать машину: ')) - 1
        except ValueError:
            print(f"Вы ввели некоректное число, пожалуйста повторите своё действие")
            Sedan_auto.sedan()
        finally:
            Sedan_auto.collor_sedan()

    def collor_sedan(self):
        try:
            type_sedan = self.gm_car_sedan[self.client_chose01]
        except IndexError:
            print(f"Вы ввели некоректное число, пожалуйста повторите своё действие")
            Sedan_auto.sedan()
        finally:
            for i, item in enumerate(type_sedan['color']):
                print(i + 1, item)
            try:
                self.client_chose02 = int(input('Отлично, теперь выберите цвет: ')) - 1
            except ValueError:
                print(f"Вы ввели некоректное число, пожалуйста повторите своё действие")
                Sedan_auto.collor_sedan()
            finally:
                Sedan_auto.position_sedan()

    def position_sedan(self):
        type_sedan = self.gm_car_sedan[self.client_chose01]
        for i, item in enumerate(type_sedan['position']):
            print(f"{i + 1}) №{item} Позиция ")
        try:
            self.client_chose03 = int(input('Превосходно, теперь выберите позицию: ')) - 1
        except ValueError:
            print(f"Вы ввели некоректное число, пожалуйста повторите своё действие")
            Sedan_auto.position_sedan()
        finally:
            print(f"""
        Вы приобрели машину типа "SEDAN" {self.gm_car_sedan[self.client_chose01]['name']}
        Цвета {self.gm_car_sedan[self.client_chose01]['color'][self.client_chose02]}
        Позиции № {self.gm_car_sedan[self.client_chose01]['position'][self.client_chose03]}
        """)


class Kupe(Gmmotors):
    def kupe(self):
        type_kupe = self.gm_car_kupe
        for i, item in enumerate(type_kupe):
            print(i + 1, item['name'])
        try:
            self.client_chose01 = int(input('Нажмите на цифру что бы выбрать машину: ')) - 1
        except ValueError:
            print(f"Вы ввели некоректное число, пожалуйста повторите своё действие")
            Kupe_auto.kupe()
        finally:
            Kupe_auto.collor_kupe()

    def collor_kupe(self):
        type_kupe = self.gm_car_sedan[self.client_chose01]
        for i, item in enumerate(type_kupe['color']):
            print(i + 1, item)
        try:
            self.client_chose02 = int(input('Отлично, теперь выберите цвет: ')) - 1
        except ValueError:
            print(f"Вы ввели некоректное число, пожалуйста повторите своё действие")
            Kupe_auto.collor_kupe()
        finally:
            Kupe_auto.position_kupe()

    def position_kupe(self):
        type_kupe = self.gm_car_kupe[self.client_chose01]
        for i, item in enumerate(type_kupe['position']):
            print(f"{i + 1}) №{item} Позиция ")
        try:
            self.client_chose03 = int(input('Превосходно, теперь выберите позицию: ')) - 1
        except ValueError:
            print(f"Вы ввели некоректное число, пожалуйста повторите своё действие")
            Kupe_auto.position_kupe()
        finally:
            print(f"""
        Вы приобрели машину типа "KUPE" {self.gm_car_kupe[self.client_chose01]['name']}
        Цвета {self.gm_car_kupe[self.client_chose01]['color'][self.client_chose02]}
        Позиции № {self.gm_car_kupe[self.client_chose01]['position'][self.client_chose03]}
        """)


class SUV(Gmmotors):
    def suv(self):
        type_suv = self.gm_car_SUV
        for i, item in enumerate(type_suv):
            print(i + 1, item['name'])
        try:
            self.client_chose01 = int(input('Нажмите на цифру что бы выбрать машину: ')) - 1
        except ValueError:
            print(f"Вы ввели некоректное число, пожалуйста повторите свои действие")
            SUV_auto.suv()
        finally:
            SUV_auto.collor_suv()

    def collor_suv(self):
        type_suv = self.gm_car_SUV[self.client_chose01]
        for i, item in enumerate(type_suv['color']):
            print(i + 1, item)
        try:
            self.client_chose02 = int(input('Отлично, теперь выберите цвет: ')) - 1
        except ValueError:
            print(f"Вы ввели некоректное число, пожалуйста повторите свои действие")
            SUV_auto.collor_suv()
        finally:
            SUV_auto.position_suv()

    def position_suv(self):
        type_suv = self.gm_car_SUV[self.client_chose01]
        for i, item in enumerate(type_suv['position']):
            print(f"{i + 1}) №{item} Позиция ")
        try:
            self.client_chose03 = int(input('Превосходно, теперь выберите позицию: ')) - 1
        except ValueError:
            print(f"Вы ввели некоректное число, пожалуйста повторите свои действие")
            SUV_auto.position_suv()
        finally:
            print(f"""
        Вы приобрели машину типа "KUPE" {self.gm_car_SUV[self.client_chose01]['name']}
        Цвета {self.gm_car_SUV[self.client_chose01]['color'][self.client_chose02]}
        Позиции № {self.gm_car_SUV[self.client_chose01]['position'][self.client_chose03]}
        """)


class Crossover(Gmmotors):
    def cross(self):
        type_cross = self.gm_car_crossover
        for i, item in enumerate(type_cross):
            print(i + 1, item['name'])
        try:
            self.client_chose01 = int(input('Нажмите на цифру что бы выбрать машину: ')) - 1
        except ValueError:
            print(f"Вы ввели некоректное число, пожалуйста повторите свои действие")
            Crossover_auto.cross()
        finally:
            Crossover_auto.collor_cross()

    def collor_cross(self):
        type_cross = self.gm_car_crossover[self.client_chose01]
        for i, item in enumerate(type_cross['color']):
            print(i + 1, item)
        try:
            self.client_chose02 = int(input('Отлично, теперь выберите цвет: ')) - 1
        except ValueError:
            print(f"Вы ввели некоректное число, пожалуйста повторите свои действие")
            Crossover_auto.collor_cross()
        finally:
            Crossover_auto.position_cross()

    def position_cross(self):
        type_cross = self.gm_car_crossover[self.client_chose01]
        for i, item in enumerate(type_cross['position']):
            print(f"{i + 1}) №{item} Позиция ")
        try:
            self.client_chose03 = int(input('Превосходно, теперь выберите позицию: ')) - 1
        except ValueError:
            print(f"Вы ввели некоректное число, пожалуйста повторите свои действие")
            Crossover_auto.position_cross()
        finally:
            print(f"""
        Вы приобрели машину типа "KUPE" {self.gm_car_crossover[self.client_chose01]['name']}
        Цвета {self.gm_car_crossover[self.client_chose01]['color'][self.client_chose02]}
        Позиции № {self.gm_car_crossover[self.client_chose01]['position'][self.client_chose03]}
        """)


Crossover_auto = Crossover()
SUV_auto = SUV()
Kupe_auto = Kupe()
Sedan_auto = Sedan()
while True:
    print("""Здраствуйте, добро пожаловать в GM MOTORS.
    1.Седан |  2.Kupe  |  3.Внедорожник  |  4.Кроссовер""")

    client_chose = input('Выберите пожалуйста type машины которую хотите приобрести: ')
    if client_chose == "1":
        Sedan_auto.sedan()
    elif client_chose == '2':
        Kupe_auto.kupe()
    elif client_chose == '3':
        SUV_auto.suv()
    elif client_chose == '4':
        Crossover_auto.cross()
    else:
        print('Выбери то что есть, а то пизды дам')

from dataclasses import dataclass
from enum import Enum
from pick import pick


class CAR_TYPE(Enum):
    UNKNOWN: str = "UNKNOWN"
    COUPET: str = "COUPET"
    SUV: str = "SUV"
    SEDAN: str = "SEDAN"

    @classmethod
    def get_types(cls):
        return [t.value for t in list(cls) if t != CAR_TYPE.UNKNOWN]


class COLOR(Enum):
    UNKNOWN: str = "UNKNOWN"
    RED: str = "RED"
    BLACK: str = "BLACK"

    @classmethod
    def get_colors(cls):
        return list(cls)

ß
class POSITION(Enum):
    UNKNOWN: str = "UNKNOWN"
    FIRST: str = "FIRST"
    SECOND: str = "SECOND"

    @classmethod
    def get_positions(cls):
        return list(cls)



@dataclass
class GM:
    """General Motors base class"""
    car_type: CAR_TYPE = CAR_TYPE.UNKNOWN
    color: COLOR = COLOR.UNKNOWN
    position: POSITION = POSITION.UNKNOWN


@dataclass
class Coupet(GM):
    car_type: CAR_TYPE = CAR_TYPE.COUPET

    def get_available_coupets(self):
        return ["MALIBU", "SPARK"]


mapper = {
    CAR_TYPE.COUPET.value: Coupet
}

def handle_user_input():
    car_type_title = "Please, choose car type: "
    selected_car_type = pick(CAR_TYPE.get_types(), car_type_title, multiselect=False, min_selection_count=1,)
    car_type_instance = mapper[selected_car_type]()

    vehicle_title = "Please, chose the car: "
    selected_vehicle = pick(car_type_instance.get_available_coupets(), car_type_title, multiselect=False, min_selection_count=1)
    print(f"You chose car type: {selected_car_type} and vehicle: {selected_vehicle}")


handle_user_input()


class SpeedCalculation:
    @staticmethod
    def calculate_allowed_speed(vehicle):
        return vehicle.get_max_speed() * vehicle.allowed_speed_ratio


class Vehicle:
    def __init__(self, max_speed, vehicle_type):
        self.max_speed = max_speed
        self.vehicle_type = vehicle_type

    def get_max_speed(self):
        return self.max_speed

    def get_type(self):
        return self.vehicle_type


class Car(Vehicle):
    def __init__(self, max_speed, vehicle_type):
        super().__init__(max_speed, vehicle_type)
        self.allowed_speed_ratio = 0.8


class Bus(Vehicle):
    def __init__(self, max_speed, vehicle_type):
        super().__init__(max_speed, vehicle_type)
        self.allowed_speed_ratio = 0.6



import random
from vehicle import Vehicle
from models import Position

COLORS = ["white", "red", "blue", "purple", "green", "yellow", "orange"]

class VehicleManager:

    def __init__(self):
        self.vehicles = []
        self.vehicle_speed = 10

    def add_vehicle_random(self):
        random_dice = random.randint(1, 6)
        if random_dice == 1:
            '''Add a vehicle only when the dice value is 1'''
            self.add_vehicle()

    def add_vehicle(self):
        vehicle_color = random.choice(COLORS)
        vehicle = Vehicle(vehicle_color)
        self.vehicles.append(vehicle)

    def move_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.move(self.vehicle_speed)
            if vehicle.is_vehicle_out_of_range():
                self.vehicles.remove(vehicle)

    def any_vehicle_colliding(self, position: Position):
        for vehicle in self.vehicles:
            if vehicle.is_colliding_with(position):
                return True

        return False

    def level_up(self):
        self.vehicle_speed += 2

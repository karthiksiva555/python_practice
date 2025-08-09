import random
from vehicle import Vehicle

COLORS = ["white", "red", "blue", "purple", "green", "yellow", "orange"]

class VehicleManager:

    def __init__(self):
        self.vehicles = []

    def add_vehicle_random(self):
        random_dice = random.randint(1, 6)
        if random_dice == 1:
            '''Add a vehicle only when the dice value is 1'''
            self.add_vehicle()

    def add_vehicle(self):
        vehicle_size = random.randint(2, 4)
        vehicle_color = random.choice(COLORS)
        vehicle = Vehicle(vehicle_size, vehicle_color)
        self.vehicles.append(vehicle)

    def move_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.move()
            if vehicle.is_vehicle_out_of_range():
                self.vehicles.remove(vehicle)


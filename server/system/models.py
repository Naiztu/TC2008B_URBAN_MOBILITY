'''

    TC2008B -  Modeling of Multi-Agent Systems with Computer Graphics

    TEAM 9

    Olivia Araceli Morales Quezada      A01707371
    Christian Leilael Rico Espinosa     A01707023
    José Ángel Rico Mendieta            A01707404

    Models for the Multi-Agent System for connecting the Unity

'''

# Import libraries
from mesa import Model

# Import Agents for the Model Street
from system.agents import car

'''
    Model for simulate the street

    Attributes:
        unique_id: ID of the street
        width: Width of the street || Number of lanes
        height: Height of the street || Measures of the street in meters
        max_num_cars: Number of cars in the street
        time: Time of the simulation
        time_stop: Time to stop the car
        range_stop: Range of execute stop car
        max_speed: Max speed of the car
'''
class ModelStreet(Model):
    # Constructor
    def __init__(self, unique_id, max_num_cars, time, time_stop, range_stop, max_speed, max_steps):
        self.unique_id = unique_id
        self.width = 3 
        self.height = 1000/5 # 1000 meters divided by 5 meters of car size
        self.max_num_cars = max_num_cars
        self.time = time
        self.time_stop = time_stop
        self.range_stop = range_stop
        self.max_speed = max_speed
        self.max_steps = max_steps
        self.step_count = 0

    # Step of the model
    def step(self):
        self.step_count += 1
        return f"Stepping the model, step number: {self.step_count}"        

    # Get information of the street
    def __str__(self):
        return f"Street ID: {self.unique_id}, Width: {self.width}, Max number of cars: {self.max_num_cars}, Time: {self.time}, Time to stop: {self.time_stop}, Range: {self.range_stop}, Max speed: {self.max_speed}, Max steps: {self.max_steps}"
    def json(self):
        return {"unique_id": self.unique_id, "width": self.width, "height": self.height, "max_num_cars": self.max_num_cars, "time": self.time, "time_stop": self.time_stop, "range_stop": self.range_stop, "max_speed": self.max_speed, "max_steps": self.max_steps}
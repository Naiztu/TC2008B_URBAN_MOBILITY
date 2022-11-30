'''

    TC2008B -  Modeling of Multi-Agent Systems with Computer Graphics

    TEAM 9

    Olivia Araceli Morales Quezada      A01707371
    Cristian Leilael Rico Espinosa     A01707023
    José Ángel Rico Mendieta            A01707404

    Models for the Multi-Agent System for connecting the Unity

'''

# Import libraries
from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
import random
from utils.converter import list_to_json

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
    def __init__(self, unique_id, max_num_cars=10, time=10000, time_stop=5000, range_stop=750, max_speed=60, max_steps=1000):
        self.unique_id = unique_id
        self.width = 3
        # 1000 meters divided by 5 meters of car size
        self.height = 1000//5
        self.grid = MultiGrid(self.width, self.height, True)
        self.max_num_cars = max_num_cars
        self.time = time
        self.time_stop = time_stop
        self.range_stop = range_stop
        self.max_speed = max_speed
        self.max_steps = max_steps
        self.step_count = 0
        self.state_ids = 0
        self.state_num_cars = 0
        self.schedule = RandomActivation(self)

    # Create cars
    def add_car(self):
        # Get the position of the car
        rail = random.randint(0, self.width - 1)
        new_car = car(self.state_ids, self, rail, 0)
        self.state_ids += 1
        # Add the car to the grid
        self.grid.place_agent(new_car, (rail, 0))
        self.schedule.add(new_car)

    # Conditional for create cars
    def random_car(self):
        if self.state_num_cars >= self.max_num_cars:
            return

        if random.randint(0, 1) == 1:
            self.add_car()
            self.state_num_cars += 1

    # Step of the model
    def step(self):
        self.step_count += 1

        # Execute the step of the cars
        self.schedule.step()
        self.random_car()

    # Get information of the street

    def __str__(self):
        return f"Street ID: {self.unique_id}, Width: {self.width}, Max number of cars: {self.max_num_cars}, Time: {self.time}, Time to stop: {self.time_stop}, Range: {self.range_stop}, Max speed: {self.max_speed}, Max steps: {self.max_steps}"

    def json(self):
        # Get position of the cars
        positions_list = []
        for idx in range(0, len(self.schedule.agents)):
            p = self.schedule.agents[idx].json()
            positions_list.append(p)
        positions = positions_list
        return {"unique_id": self.unique_id, "width": self.width, "height": self.height, "max_num_cars": self.max_num_cars, "time": self.time, "time_stop": self.time_stop, "range_stop": self.range_stop, "max_speed": self.max_speed, "max_steps": self.max_steps, "positions": positions, "step_count": self.step_count}

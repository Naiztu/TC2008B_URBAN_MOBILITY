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
from mesa.space import SingleGrid
from mesa.time import SimultaneousActivation
from mesa.datacollection import DataCollector
import random
import numpy as np

# Import Agents for the Model Street
from system.agents import car

def get_grid(model):
    grid = np.zeros((model.grid.width, model.grid.height))
    for agent in model.schedule.agents:
        if agent.state == 0:
            continue
        x, y = agent.pos
        grid[x][y] = 2 if agent.direction == 1 else 1
    return grid



'''
    Model for simulate the street

    Parameters:
        unique_id: ID of the street
        width: Width of the street || Number of lanes
        height: Height of the street || Measures of the street in meters
        max_num_cars: Number of cars in the street
        time: Time of the simulation in minutes
        time_stop: Time to stop the car in minutes
        range_stop: Range of execute stop car in meters
        max_speed: Max speed of the car in km/h
        no_change_rail: Flah if change the 
        
    Attributes:
        Schedule: Schedule of the model
        Grid: Grid of the model
        state_num_cars: Number of cars in the street
        step_count: Steps of the simulation
        state_ids: ID of the cars in the street
        state_num_cars: Number of cars in the street

'''


class ModelStreet(Model):
    # Constructor
    def __init__(self, unique_id, width=3, height=1000, max_num_cars=1000,
    time=10, time_stop=5, range_stop=750, max_speed=60, no_change_rail = True):
        self.unique_id = unique_id
        self.width = width 
        self.height = int(height // 5) # 5 meters per cell
        self.max_num_cars = max_num_cars
        self.grid = SingleGrid(self.width, self.height, False)
        self.time_stop = time_stop * 60 # Convert to seconds
        self.range_stop = int(range_stop // 5) # 5 meters per cell
        self.max_speed = int(max_speed // (3.6*5))  # Convert to meters per second
        self.max_steps = time * 60
        self.step_count = 0
        self.state_ids = 0
        self.state_num_cars = 0
        self.flag_stop = False
        self.no_change_rail = no_change_rail
        self.num_cars_is_out = 0
        self.schedule = SimultaneousActivation(self)
        self.datacollector = DataCollector(model_reporters={"Grid": get_grid})

    # Create cars
    def add_car(self):
        # Get the position of the car
        rail = random.randint(0, self.width - 1)
        if not self.grid.is_cell_empty((rail, 0)):
            return
        new_car = car(self.next_id(), self, self.max_speed, 1, 1, self.no_change_rail)
        # Add the car to the grid
        self.grid.place_agent(new_car, (rail, 0))
        self.schedule.add(new_car)

    # Conditional for create cars
    def random_car(self):
        if self.state_num_cars >= self.max_num_cars:
            return

        self.add_car()
        self.state_num_cars += 1

    def clean_deaths(self):
        for agent in self.schedule.agents:
            if agent.state == 0:
                self.num_cars_is_out += 1
                self.schedule.remove(agent)
                self.grid.remove_agent(agent)
                self.state_num_cars -= 1
    
    def select_car_to_stop(self):
        if self.flag_stop:
            return

        if self.time_stop > self.step_count:
            return

        list_cars = []
        for agent in self.schedule.agents:
            if agent.pos[1] >= self.range_stop:
                list_cars.append(agent)

        if len(list_cars) == 0:
            return

        car = random.choice(list_cars)

        car.direction = 0
        self.flag_stop = True


    def is_finished(self):
        return self.step_count >= self.max_steps

    # Step of the model
    def step(self):
        self.datacollector.collect(self)

        # Execute the step of the cars
        self.schedule.step()
        self.clean_deaths()
        self.random_car()
        self.select_car_to_stop()
        self.step_count += 1

    def next_id(self):
        self.state_ids += 1
        return self.state_ids

    # Get information of the street
    def json(self):
        # Get position of the cars
        positions_list = []
        for idx in range(0, len(self.schedule.agents)):
            p = self.schedule.agents[idx].json()
            positions_list.append(p)
        positions = positions_list
        return {"unique_id": self.unique_id, "width": self.width, "height": self.height, "max_num_cars": self.max_num_cars, "time_stop": self.time_stop, 
                "range_stop": self.range_stop, "max_speed": self.max_speed, "max_steps": self.max_steps, "positions": positions, "step_count": self.step_count, "state_ids": self.state_ids, 
                "state_num_cars": self.state_num_cars, "num_cars_is_out": self.num_cars_is_out}


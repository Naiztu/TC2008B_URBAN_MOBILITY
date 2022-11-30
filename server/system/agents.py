'''

    TC2008B -  Modeling of Multi-Agent Systems with Computer Graphics

    TEAM 9

    Olivia Araceli Morales Quezada      A01707371
    Cristian Leilael Rico Espinosa     A01707023
    José Ángel Rico Mendieta            A01707404

    Agents for the Multi-Agent System for connecting the Unity

'''

# Import libraries
from mesa import Agent
import numpy as np


'''
    Agent for simulate the car

    Attributes:
        unique_id: ID of the car
        position: Position of the car
        speed: Speed of the car
        direction: Direction of the car
'''


class car(Agent):
    # Constructor
    def __init__(self, unique_id, model, x=0, y=0, speed=1, direction=1):
        super().__init__(unique_id, model)
        self.unique_id = unique_id
        self.position = np.array([x, y], dtype=np.int32)
        self.speed = speed
        self.direction = direction

    def finished(self):
        if self.position[1] == self.model.grid.heigth:
            self.model.grid.remove_agent(self)
            self.model.state_num_cars -= 1
            self.model.schedule.remove(self)
            return True

    def step(self):
        self.position = np.array(
            [self.position[0], self.position[1] + self.speed], dtype=np.int32)

    # Get information of the car

    def __str__(self):
        return f"Car ID: {self.unique_id}, Position: {self.position}, Speed: {self.speed}, Direction: {self.direction}"

    def json(self):
        return {"unique_id": self.unique_id, "position": {"x": int(self.position[0]), "y": int(self.position[1])}, "speed": self.speed, "direction": self.direction}

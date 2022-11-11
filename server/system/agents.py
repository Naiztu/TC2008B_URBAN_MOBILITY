'''

    TC2008B -  Modeling of Multi-Agent Systems with Computer Graphics

    TEAM 9

    Olivia Araceli Morales Quezada      A01707371
    Christian Leilael Rico Espinosa     A01707023
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
    def __init__(self, unique_id, x, y, speed, direction):
        self.unique_id = unique_id
        self.position = np.array(x, y, 0)
        self.speed = speed
        self.direction = direction

    # Get information of the car

    def __str__(self):
        return f"Car ID: {self.unique_id}, Position: {self.position}, Speed: {self.speed}, Direction: {self.direction}"

    def json(self):
        return {"unique_id": self.unique_id, "position": self.position, "speed": self.speed, "direction": self.direction}

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
        width: Width of the street
        height: Height of the street
'''
class ModelStreet(Model):
    # Constructor
    def __init__(self, unique_id, width, legth):
        self.unique_id = unique_id
        self.width = width
        self.legth = legth

    # Get information of the street
    def __str__(self):
        return f"Street ID: {self.street_id}, Width: {self.width}, Length: {self.legth}"
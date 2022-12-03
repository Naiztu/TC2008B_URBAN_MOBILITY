'''

    TC2008B -  Modeling of Multi-Agent Systems with Computer Graphics

    TEAM 9

    Olivia Araceli Morales Quezada      A01707371
    Cristian Leilael Rico Espinosa     A01707023
    José Ángel Rico Mendieta            A01707404

    Server for the Multi-Agent System for connecting the Unity

'''

# Import libraries
from flask import Flask, request
from system.models import ModelStreet
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from utils.converter import message_to_json, position_to_json, to_json

# Create the Flask app
app = Flask(__name__)

# Initialize the model (unique_id, width, height, max_num_cars, time, time_stop, range_stop, max_speed, no_change_rail)
model_initial = ModelStreet(unique_id=1,width=3, height=1000, max_num_cars=999, time=10, time_stop=5, range_stop=750, max_speed=60, no_change_rail = False)

model = model_initial

# Endpoint for check the status of the server
@app.route('/', methods=['GET'])
def hello_world():
    return message_to_json("The app is running!")

# Initialize the model
@app.route('/init', methods=['POST'])
def initial_model():
    # Get the parameters
    heigth = request.json['heigth']
    width = request.json['width']
    max_num_cars = request.json['max_num_cars']
    time = request.json['time']
    time_stop = request.json['time_stop']
    range_stop = request.json['range_stop']
    max_speed = request.json['max_speed']
    no_change_rail = request.json['no_change_rail']

    # Initialize the model
    global model
    model = ModelStreet(1, width, heigth, max_num_cars, time, time_stop, range_stop, max_speed,no_change_rail)

    # Return the message
    return to_json(model.json())

# Reset state of the model
@app.route('/reset', methods=['GET'])
def reset_model():

    global model
    model = model_initial
    return message_to_json('Reset the model')

# Exexute step of model
@app.route('/step', methods=['GET'])
def step_model():
    model.step()
    return to_json(model.json())



# Get initial info of model
@app.route('/info', methods=['GET'])
def info_model():
    return to_json(model.json())


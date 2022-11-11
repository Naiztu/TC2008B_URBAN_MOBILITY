'''

    TC2008B -  Modeling of Multi-Agent Systems with Computer Graphics

    TEAM 9

    Olivia Araceli Morales Quezada      A01707371
    Christian Leilael Rico Espinosa     A01707023
    José Ángel Rico Mendieta            A01707404

    Server for the Multi-Agent System for connecting the Unity

'''

# Import libraries
from flask import Flask, request
from system.models import ModelStreet
from utils.converter import message_to_json, position_to_json, to_json

# Create the Flask app
app = Flask(__name__)

# Initialize the model (unique_id, max_num_cars, time, time_stop, range_stop, max_speed, max_steps)
model = ModelStreet(1, 10, 10, 5, 5, 5, 1000)

# Endpoint for check the status of the server
@app.route('/',methods=['GET'])
def hello_world():
    return message_to_json("The app is running!")

# Initialize the model
@app.route('/init',methods=['POST'])
def initial_model():
    # Get the parameters
    max_num_cars = request.json['max_num_cars']
    time = request.json['time']
    time_stop = request.json['time_stop']
    range_stop = request.json['range_stop']
    max_speed = request.json['max_speed']
    max_steps = request.json['max_steps']

    # Initialize the model
    global model
    model = ModelStreet(1, max_num_cars, time, time_stop, range_stop, max_speed, max_steps)

    # Return the message
    return to_json(model.json())

# Reset state of the model
@app.route('/reset',methods=['GET'])
def reset_model():

    global model
    model = ModelStreet(1, 10, 10, 5, 5, 5, 1000)

    return message_to_json('Reset the model')

# Exexute step of model
@app.route('/step',methods=['GET'])
def step_model():
    return message_to_json(model.step())

# Get initial info of model
@app.route('/info',methods=['GET'])
def info_model():
    return message_to_json(model.__str__())

# Save animation of model
@app.route('/save',methods=['GET'])
def save_model():
    return message_to_json('Saving the app')



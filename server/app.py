'''

    TC2008B -  Modeling of Multi-Agent Systems with Computer Graphics

    TEAM 9

    Olivia Araceli Morales Quezada      A01707371
    Christian Leilael Rico Espinosa     A01707023
    José Ángel Rico Mendieta            A01707404

    Server for the Multi-Agent System for connecting the Unity

'''

# Import libraries
from flask import Flask, jsonify
from system.models import ModelStreet
from utils.converter import message_to_json, position_to_json

# Create the Flask app
app = Flask(__name__)

# Initialize the model
model = ModelStreet(1, 10, 10)

# Endpoint for check the status of the server
@app.route('/')
def hello_world():
    return message_to_json("The app is running!")

# Initialize the model
@app.route('/init')
def initial_model():
    return message_to_json("The model has been initialized")

# Reset state of the model
@app.route('/reset')
def reset_model():
    return message_to_json('Resetting the app')

# Exexute step of model
@app.route('/step')
def step_model():
    return message_to_json('Stepping the app')

# Get initial info of model
@app.route('/info')
def info_model():
    return message_to_json(model.__str__())

# Save animation of model
@app.route('/save')
def save_model():
    return message_to_json('Saving the app')
    


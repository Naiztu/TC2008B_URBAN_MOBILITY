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

# Initialize the model (unique_id, width, heigth, max_num_cars, time, time_stop, range_stop, max_speed, max_steps)
model = ModelStreet(unique_id=1,width=3, heigth=1000, max_num_cars=30, time=10, time_stop=5, range_stop=750, max_speed=60, max_steps=10000)

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
    max_steps = request.json['max_steps']

    # Initialize the model
    global model
    model = ModelStreet(1, width, heigth, max_num_cars, time, time_stop, range_stop, max_speed, max_steps)

    # Return the message
    return to_json(model.json())

# Reset state of the model
@app.route('/reset', methods=['GET'])
def reset_model():

    global model
    model = ModelStreet(1, 3, 1000, 30, 10, 5, 750, 60, 300)

    return message_to_json('Reset the model')

# Exexute step of model
@app.route('/step', methods=['GET'])
def step_model():
    model.step()
    return model.json()

# Get initial info of model
@app.route('/info', methods=['GET'])
def info_model():
    return message_to_json(model.__str__())

# Save animation of model
@app.route('/save', methods=['GET'])
def save_model():
    while(model.step_count != model.max_steps):
        model.step()

    all_grids = model.datacollector.get_model_vars_dataframe()

    fig, axis = plt.subplots(figsize=(60, 3))
    axis.set_xticks([])
    axis.set_yticks([])
    patch = axis.imshow(all_grids.iloc[0][0], cmap=plt.cm.binary)


    def animate(i):
        patch.set_data(all_grids.iloc[i][0])


    anim = animation.FuncAnimation(
        fig, animate, frames=len(all_grids), interval=100)
    anim.save('animation.gif', writer='imagemagick', fps=10)

    reset_model()
    return message_to_json('Saving the app')

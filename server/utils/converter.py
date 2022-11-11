'''

    TC2008B -  Modeling of Multi-Agent Systems with Computer Graphics

    TEAM 9

    Olivia Araceli Morales Quezada      A01707371
    Christian Leilael Rico Espinosa     A01707023
    José Ángel Rico Mendieta            A01707404

    Converters functions for the Multi-Agent System for connecting the Unity

'''

# Import libraries
from flask import jsonify

# Convert message to json
def message_to_json(message):
    return jsonify({"message": message})

# Convert list of cars to json
def position_to_json(position):
    return jsonify({'x': position.x, 'y': position.y})

# Convert object to json
def to_json(obj):
    return jsonify(obj)

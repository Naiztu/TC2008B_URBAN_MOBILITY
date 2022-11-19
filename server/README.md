<a href="#">
    <img src="https://javier.rodriguez.org.mx/itesm/2014/tecnologico-de-monterrey-black.png" alt="ITESM" title="ITESM" align="right" height="60" />
</a>

# **TC2008B_URBAN_MOBILITY - SERVER**

Server for the Multi-Agent System for connecting the Unity

## Structure

app - Contains endpoint and server settings.

system - Contains the model and agent classes for simulation interaction.

utils - Contains useful functions.

## Execution

### Development environment

```text
pip install virtualenv
python -m venv venv
venv\Scripts\Activate.ps1
pip install mesa matplob numpy pandas flask
pip install -r https://raw.githubusercontent.com/projectmesa/mesa/main/examples/boltzmann_wealth_model/requirements.txt
flask --app app.py --debug run
```

### Production enviroment

```text
pip install mesa matplob numpy pandas flask
flask --app app.py run
```

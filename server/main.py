from system.models import ModelStreet
import matplotlib.animation as animation
import matplotlib.pyplot as plt

model = ModelStreet(unique_id=1,width=3, height=300, max_num_cars=500, time=10, time_stop=1, range_stop=200, max_speed=60)


while not model.is_finished():
    model.step()

all_grids = model.datacollector.get_model_vars_dataframe()


fig, axis = plt.subplots()

def animate(i):
    axis.imshow(all_grids.iloc[i][0])
    axis.set_axis_off()

anim = animation.FuncAnimation(
    fig, animate, frames=model.max_steps, interval=100)

plt.show()
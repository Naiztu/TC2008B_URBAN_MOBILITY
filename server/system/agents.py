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


'''
    Agent for simulate the car

    Attributes:
        unique_id: ID of the car
        model: Model of the car
        pos: Position of the car
        speed: Speed of the car
        direction: Direction of the 
        state: State of the car

'''


class car(Agent):
    # Constructor
    def __init__(self, unique_id, model, speed=1, direction=1, state=1):
        super().__init__(unique_id, model)
        self.speed = speed  
        self.direction = direction
        self.state = state
        self.ratio = speed + 1
        self.new_position = None
        self.new_state = None
        self.change_rail = None
        self.options = [1, -1]


    def is_in_range(self, x, y):
        if self.model.grid.out_of_bounds((x, y)):
            self.new_state = 0
            return False
        return True

    def change_direction(self):
        if self.direction == 0:
            return
        
        for i in range(1, self.ratio):
            x = self.pos[0]
            y = self.pos[1] + i 

            if self.model.grid.out_of_bounds((x, y)):
                return

            if self.model.grid.is_cell_empty((x, y)):
                continue 

            direction_of_car_in_front = self.model.grid[x][y].direction
            if direction_of_car_in_front == 1:
                break
            
            for j in self.options:
                x = self.pos[0] + j

                if self.model.grid.out_of_bounds((x, y)):
                    continue

                flag = True
                for N in self.model.grid.get_neighbors((x, y), moore=True, include_center=True, radius=self.ratio):
                    if N.new_position == (x, y):
                        flag = False
                        break
                if flag:
                    self.new_position = (x, y)
                    return

    # Step of the car
    def step(self):
        
        

        self.new_position = (self.pos[0], self.pos[1] + self.speed * self.direction)
        if not self.is_in_range(self.new_position[0], self.new_position[1]):
            self.new_position = None
            return self.json()
        self.change_direction()
        if not self.model.grid.is_cell_empty(self.new_position):
            self.new_position = None
            return self.json()
        
        
    def advance(self):
        
        if self.new_position is not None and self.model.grid.is_cell_empty(self.new_position):
            self.model.grid.move_agent(self, self.new_position)
            self.new_position = None
        self.state = self.new_state

    # Get information of the car
    def json(self):
        return {"unique_id": self.unique_id, "pos": {"x": self.pos[0],
        "y": self.pos[1]}, "speed": self.speed, "direction": self.direction}

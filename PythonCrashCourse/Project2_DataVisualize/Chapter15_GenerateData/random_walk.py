# ----------------------
# Author: blateyang
# Date: 2018/3/12
# ----------------------
from random import choice


class RandomWalk():
    """A class which can generate data of random walk"""
    def __init__(self, num_points=5000):
        """Initialize attribute of random walk"""
        self.num_points = num_points
        # all random walk start from (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """get distance and direction of each random walk"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction*distance
        return step

    def fill_walk(self):
        """Generate random walk data"""
        while len(self.x_values) < self.num_points:
            # decide proceeding direction and distance toward it
            x_step = self.get_step()
            y_step = self.get_step()

            # reject not proceed
            if x_step == 0 and y_step == 0:
                continue
            # calculate x and y of next point
            next_x = self.x_values[-1]+x_step
            next_y = self.y_values[-1]+y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


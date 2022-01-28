from math import sqrt
from DrawingPanel import *

# assumption: choose units for the system such that G is 1 and the mass of Earth is 1

# constants for the gravitational constant and time step
G = 1
T = 1

# initialize panel for drawing system
p = DrawingPanel(1500, 1000, background = "black")

# System represents a collection of bodies gravitationally interacting with each other.
class System:
    """
        PARAMS:
            bodies: list of Body objects
    """
    def __init__(self, bodies):
        self.bodies = bodies

    """
        Calculates the x- and y-acceleration for a body in the system.
        PARAMS:
            index: index of the body to have its acceleration calculated
        RETURN:
            tuple with two elements, representing the x- and y-components of acceleration
    """
    def calculate_acceleration(self, index):
        current = self.bodies[index]
        ax = 0
        ay = 0

        for i in range(len(self.bodies)):
            if i != index:
                other = self.bodies[i]
                r = sqrt((current.x - other.x) ** 2 + (current.y - other.y) ** 2)
                ax += (G * other.mass / r ** 3) * (other.x - current.x)
                ay += (G * other.mass / r ** 3) * (other.y - current.y)

        return (ax, ay)

    """
        Adjusts the velocities of all of the bodies in the system.
    """
    def calculate_velocity(self):
        for i in range(len(self.bodies)):
            current = self.bodies[i]
            a = self.calculate_acceleration(i)
            current.vx += a[0] * T
            current.vy += a[1] * T

    """
        Change the x- and y-positions of all of the bodies in the system.
    """
    def update_positions(self):
        for body in self.bodies:
            body.x += body.vx * T
            body.y += body.vy * T

    """
        Carry out one time step.
    """
    def advance_time(self):
        self.calculate_velocity()
        self.update_positions()
        self.plot_system()

    """
        Draw the system.
    """
    def plot_system(self):
        p.clear()
        
        for body in self.bodies:
            p.fill_oval(body.x, body.y, 10, 10, body.color)
        
        p.show()
        p.sleep(10)

from Body import Body
from System import System

def main():
    # initial bodies of sun-like star and two Jupiter-like planets
    s1 = Body(1000000, 750, 500, nm = "S1", color = "yellow")
    p1 = Body(1000, 1250, 500, vy = -40, nm = "P1", color = "orange")
    p2 = Body(1000, 1000, 500, vy = -60, nm = "P2", color = "blue")
    # TODO: add a new Jupiter-like body here; Earth mass is taken as 1; see Body class for clarification of parameters
    
    # initialize system with list of bodies
    s = System([s1, p1, p2]) # TODO: add your new body to the list of bodies in the system

    # draw initial system
    s.plot_system()

    # carry out 1000 time steps
    for n in range(1000):
        s.advance_time()

main()
# print statement shows when simulation is complete
print("done")

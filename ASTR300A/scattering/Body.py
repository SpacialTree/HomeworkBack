class Body:
    # Body represents any celestial body in a solar system, possessing attributes for its mass, position, velocity, and name.
            
    """
        PARAMS:
            m: mass of the body
            x: initial x-position of the body
            y: initial y-position of the body
            vx: optional initial x-velocity
            vy: optional initial y-velocity
            nm: optional name
            color: optional color as a string
    """
    def __init__(self, m, x, y, vx = 0, vy = 0, nm = "", color = "white"):
        self.mass = m
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.name = nm
        self.color = color

    def __str__(self):
        name = ""

        if self.name != "":
            name = self.name
        else:
            name = "Body"

        return "{}(mass={},x={},y={},vx={},vy={})".format(name, self.mass, self.x, self.y, self.vx, self.vy)

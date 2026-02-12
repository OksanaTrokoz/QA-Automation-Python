class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == 'side_a':
            if value > 0:
                super().__setattr__(name, value)
        elif name == 'angle_a':
            if 0 < value < 180:
                super().__setattr__(name, value)
                super().__setattr__("angle_b", 180 - value)
        elif name == 'angle_b':
            if 0 < value < 180:
                super().__setattr__(name, value)
                super().__setattr__("side_a", value)
        else:
            super().__setattr__(name, value)


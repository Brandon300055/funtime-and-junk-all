class Location(object):
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def get_loc(self):
        return [self.x, self.y]

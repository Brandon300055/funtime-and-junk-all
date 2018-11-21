#1
class Battery:
    def __init__(self, capacity):
        self.capacity = capacity
        self.charge = capacity
#2
    def getCapacity(self):
        return self.capacity
#3
    def getCharge(self):
        return self.charge
#4
    def drain(self, milliamps):
        charge = self.charge
        if (milliamps > 0) and (self.charge > 0):
            self.charge = (self.charge - milliamps)
            if (self.charge <= 0):
                self.charge = self.capacity
            return True
        return False
#5
    def recharge(self, milliamps):
        charge = self.charge
        if (milliamps > 0) and (self.charge < self.capacity):
            self.charge = (self.charge + milliamps)
            if (self.charge >= self.capacity):
                self.charge = self.capacity
            return True
        return False


#6
class Rectangle:
    def __init__(self, x, y, width, height):
        self.y = y
        self.x = x
        self.width = width
        self.height = height
#7
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
#8
    def setX(self, value):
        if self.x != value:
            self.x = value
            if (self.x <= 0):
                self.x = 0
                return False
        return True

    def setY(self, value):
        if self.y != value:
            self.y = value
            if (self.y <= 0):
                self.y = 0
                return False
        return True

    def setWidth(self, value):
        if self.width != value:
            self.width = value
            if (self.width <= 0):
                self.width = 0
                return False
        return True

    def setHeight(self, value):
        if self.height != value:
            self.height = value
            if (self.height <= 0):
                self.height = 0
                return False
        return True

r = Rectangle(1,2,3,4)
print(r.setX(10))# -> True
print(r.getX())# -> 10
print(r.setX(0))# -> False
print(r.getX())# -> 0
print(r.setX(-1))# -> False
print(r.getX())# -> 0
print(r.setX(99999999))# -> True
print(r.getX())# -> 99999999

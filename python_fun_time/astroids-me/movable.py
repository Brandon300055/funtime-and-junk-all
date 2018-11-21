class Movable:
    def __init__(self, mX, mY, mDX, mDY, mWorldWidth, mWorldHeight):
        self.mX = mX
        self.mY = mY
        self.mDX = mDX
        self.mDY = mDY
        self.mWorldWidth = mWorldWidth
        self.mWorldHeight = mWorldHeight

    def getX():
        return self.mX
    def getY():
        return self.mY
    def getDX():
        return self.mDX
    def getDY():
        return self.mDY
    def getWorldWidth():
        return self.mWorldWidth
    def getWorldHeight():
        return self.mWorldHeight
    def move(dt):
        return dt 
    def accelerate(self):
        raise NotImplementedError
    def evolve(self):
        raise NotImplementedError
    def draw(self):
        raise NotImplementedError

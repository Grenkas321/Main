class Rectangle:
    x1, x2, y1, y2 = 0, 0, 0, 0

    rectcnt = 0

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.__class__.rectcnt += 1
        setattr(self, f"rect_{self.rectcnt}", self.rectcnt)

    def __str__(self):
        return f"{(self.x1,self.y1)}{(self.x1,self.y2)}{(self.x2,self.y2)}{(self.x2,self.y1)}\n count = {self.rectcnt}"

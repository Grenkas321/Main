class Rectangle:
    rectcnt = 0
    
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
        Rectangle.rectcnt += 1
    
        field_name = f"rect_{Rectangle.rectcnt}"
        setattr(self, field_name, Rectangle.rectcnt)
    
    def __str__(self):
        coordinates = f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1})"
        return f"{coordinates} [Rectangle count: {Rectangle.rectcnt}]"
    
    def __lt__(self, other):
        return self.area() < other.area()
    
    def __eq__(self, other):
        return self.area() == other.area()
    
    def __abs__(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)

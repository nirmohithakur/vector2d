class Vector2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2d((self.x) = x, (self.y) = y)"
    
    def __str__(self):
        return f"{self.x}i + {self.y}j"
    
    def __abs__(self):
        return ((self.x)**2) + (self.y)**2))**(1/2))
    
    def __neg__(self):
        return f"Vector2d(-(self.x), -(self.y))"
    
    def __add__(self, other):
        return Vector2d(self.x +other.x, self.y + other.y)
                        
    def __eq__(self,other):
        return (self.x, self.y) == (other.x, other.y)
    
    def __sub__(self, other):
        return Vector2d((self.x - other.x), (self.y - other.y))
    
    def angle(self):
        tan = math.atan2((self .y), (self.x))
        return math.degrees(tan)

    
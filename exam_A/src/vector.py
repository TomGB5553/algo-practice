class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y


 
    def __add__(self,other):
        return Vector2D(self.x+other.x, self.y+other.y)
    
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"


 
    def norm_squared(self):
        return self.x*self.x + self.y*self.y
    def __lt__(self, other):
        return self.norm_squared()<other.norm_squared()        #self.method !!! and nothing in parentheses !!!!
    def __mul__(self, k):
        return Vector2D(self.x*k, self.y*k)
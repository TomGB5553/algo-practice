class Polynomial():
    def __init__(self, coeffs):
        self.coeffs = coeffs
        
    def __repr__(self):
        return f"Polynomial({self.coeffs})"     #why the F ??!
    
    def degrees(self):
        degree=-1
        if len(self.coeffs)==0:
            return degree
        for i in self.coeffs:
            if self.coeffs[i] != 0:
                degree=i
        return degree
    
    def evaluate(self, x):
        out=0
        for i in self.coeffs:
            out += x**i
        return out
    
    def __add__(self, other):
        new_coef=[]
        n =max(len(self.coeffs), len(other.coeffs))
        for i in n:
            a = self.coeffs[i] if i < len(self.coeffs) else 0
            b = other.coeffs[i] if i < len(other.coeffs) else 0
            new_coef.append(a+b)
        return Polynomial(new_coef)
    
    def __mul__(self, other):
        
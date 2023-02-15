class Calc:
    a = 0
    b = 0
    def __init__(Self,a,b):
        Self.a = a
        #Self.b = b
    
    def suma(Self):
        return Self.a+Self.b

    def resta(Self):
        return Self.a-Self.b
    
    def prod(Self):
        return Self.a*Self.b
    
    def div(Self):
        if Self.b == 0.0:
            raise ZeroDivisionError
        return Self.a/Self.b
    
    def mod(Self):
        return Self.a%Self.b

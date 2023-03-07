class Media:
    arrayNotas=[]
    
    def notas(self):
        return self.arrayNotas

    def add(self, numbrer):
        if numbrer <= 0 or numbrer >=20:
            raise ValueError
        self.arrayNotas.append(numbrer)
    
    def media(self):
        suma = 0
        for i in self.arrayNotas:
            suma += i
        return suma/len(self.arrayNotas)
    
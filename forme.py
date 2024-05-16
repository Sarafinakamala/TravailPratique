class Forme:
    def __init__(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
class Triangle(Forme):
    def aire(self):
        return (self.largeur * self.hauteur)/2
class Rectangle(Forme):
    def aire(self):
        return self.largeur * self.hauteur
rectangle = Rectangle(8,12)
print(f"L' aire du rectangle est de: {rectangle.aire()}")
triangle = Triangle(5,10)
print(f"L' aire du triangle est de: {triangle.aire()}")

from math import sqrt

class Vector2D:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self,new_x):
        self.__x = new_x
    @y.setter
    def y(self,new_y):
        self.__y = new_y

    # Methode pour calculer la norme
    def norme(self):
        return sqrt(self.__x**2+self.__y**2) 

    # Methode pour faire l'adition
    def addition(self,t):
        self.__x += t.x
        self.__y += t.y 

    # Methode pour faire une soustraction
    def soustraction(self,t):
        self.__x -= t.x
        self.__y -= t.y

    # Methode pour faire le produit scalaire
    def produit_scalaire(self,t):
        return self.__x * t.x + self.__y * t.y 

    # Methode pour verifier la colinearité entre deux vecteurs
    def colinearite(self,t):
        if((self.__x*t.y-self.y*t.x)==0):
            print("ils sont colinéaires")
        else:
            print("Ils sont pas colinéaires")


v1 = Vector2D(2,5)
print(v1.norme())

v2 = Vector2D(5,2)
v1.addition(v2)

print(v1.x, v1.y, sep ='\n')

v1.soustraction(v2)
print(v1.x, v1.y, sep ='\n')

v1.colinearite(v2)
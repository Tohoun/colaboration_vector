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

    def norme2(self):
        """Methode pour calculer la norme"""
        return sqrt(self.__x**2+self.__y**2) 

    def addition(self,t):
        """Methode effectuant l'addition"""
        self.__x += t.x
        self.__y += t.y 

    def soustraction(self,t):
        """Methode effectuant la soustraction"""
        self.__x -= t.x
        self.__y -= t.y

    def produit_scalaire(self,t):
        """Methode effectuant le produit scalaire"""
        return self.__x * t.x + self.__y * t.y 

    def colinearite(self,t):
        """verification de la colinéarité"""
        return self.produit_scalaire(t)==0

    def unitaire(self):
        """verification du caractère unitaire"""
        return self.norme2()==1


v1 = Vector2D(2,5)
print(v1.norme2())

v2 = Vector2D(5,2)
v1.addition(v2)

print(v1.x, v1.y, sep ='\n')

v1.soustraction(v2)
print(v1.x, v1.y, sep ='\n')

print(v1.colinearite(v2))
print(v1.unitaire())
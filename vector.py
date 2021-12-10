import math
class Vector:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def norme(self):
        n = math.sqrt(self.__x**2+self.__y**2)
        print(n)

v1 = Vector(2,5)
v1.norme()
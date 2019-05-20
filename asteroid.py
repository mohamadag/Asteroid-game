#########################
# FILE : asteroid.py
#WRITER: mohamed ,mohamedag,314720293,mohamed,muhammad.krad,318577335
#EXERCISE: intro2cs ex9 2016-2017
#DESCRIPTION : class Asteroid
########################
import random
import math
TO_RADIOUS_1=10
TO_RADIOUS_2=5
class Asteroid:
    def __init__(self,place_x,place_y,size):
        self.__place_x=place_x
        self.__place_y=place_y
        self.__speed_x=random.randrange(1,10)
        self.__speed_y=random.randrange(1,10)
        self.__size=size

    def get_place_x(self):
        ' return place x '
        return self.__place_x

    def get_place_y(self):
        ' return place y'
        return self.__place_y

    def get_speed_x(self):
        ' return speed x'
        return self.__speed_x

    def get_speed_y(self):
        ' return speed y'
        return self.__speed_y

    def get_size(self):
        ' return size '
        return self.__size

    def set_place_x(self,new_place_x):
        ' change place x'
        self.__place_x=new_place_x

    def set_place_y(self,new_place_y):
        ' change place y'
        self.__place_y=new_place_y

    def set_speed_x(self,new_speed_x):
        ' change speed x'
        self.__speed_x=new_speed_x

    def set_speed_y(self,new_speed_y):
        ' change speed y'
        self.__speed_y=new_speed_y

    def set_size(self,new_size):
        ' change size'
        self.__size=new_size

    def radious(self):
        ' return radious'
        return self.__size*TO_RADIOUS_1-TO_RADIOUS_2

    def has_intersection(self, obj):
        ''' cheek if the objects intersection with asteroid  '''
        distance=math.sqrt(((obj.get_place_x()-self.__place_x)**2)+((obj.get_place_y()-self.__place_y)**2))
        if distance<=self.radious()+obj.radious():
            return True
        else:
            return False

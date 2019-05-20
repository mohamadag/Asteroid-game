
SHIP_LIFE=3
SHIP_RADIOUS=1
class Ship:

    def __init__(self,place_x,place_y):
        self.__place_x=place_x
        self.__place_y=place_y
        self.__speed_x=0
        self.__speed_y=0
        self.__direction=0.0
        self.__life=SHIP_LIFE


    def get_place_x(self):
        ' return place x'
        return self.__place_x

    def get_place_y(self):
        ' return place y'
        return self.__place_y

    def get_speed_x(self):
        ' return speed x'
        return self.__speed_x

    def get_speed_y(self):
        'return speed y'
        return self.__speed_y

    def get_direction(self):
        ' return direction'
        return self.__direction

    def get_life(self):
        'return ship life'
        return self.__life


    def set_place_x(self,new_place_x):
        ' change place x '
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

    def set_direction(self,new_direction):
        ' change direction'
        self.__direction=new_direction

    def set_life(self,new_life):
        ' change life '
        self.__life=new_life


    def radious(self):
        ' return ship radious'
        return SHIP_RADIOUS

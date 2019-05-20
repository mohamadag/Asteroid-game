#########################
# FILE : asteroids_main.py
#WRITER: mohamed ,mohamedag,314720293,mohamed,muhammad.krad,318577335
#EXERCISE: intro2cs ex9 2016-2017
#DESCRIPTION : game loop
########################
from screen import Screen
import sys
from ship import Ship as sh
from asteroid import Asteroid
from torpedo import Torpedo
import math
import random
DEFAULT_ASTEROIDS_NUM = 5
RIGHT=-7
LEFT=7
ASTERIODS_SIZE=3
TORPEDO_LIMIT=15
MAX_POINTS=100
MID_POINTS=50
MIN_POINTS=20
TORPEDO_LIFE_LIMIT=200
ASTEROID_MAX_SIZE=3
ASTEROID_MID_SIZE=2
ASTEROID_MIN_SIZE=1

class GameRunner:

    def __init__(self, asteroids_amnt):
        self._screen = Screen()
        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        place_x = random.randrange(1, self.screen_max_x)
        place_y = random.randrange(1, self.screen_max_y)
        self.ship1 = sh(place_x, place_y)
        self.asteroids_amnt=asteroids_amnt
        self.ast_lst=[]
        self.torp_lst=[]
        i=0
        self.__value=0
        #creat asteroid
        while i < asteroids_amnt:
            place_x = random.randrange(1,self.screen_max_x)
            place_y = random.randrange(1,self.screen_max_y)
            ast=Asteroid(place_x,place_y,ASTERIODS_SIZE)
            if ast.has_intersection(self.ship1)==False:
                self.ast_lst.append(ast)
                self._screen.register_asteroid(self.ast_lst[i],ASTERIODS_SIZE)
                i+=1


    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop,5)

    def move_obj(self,obj):

        ''' this func used to move object using a formula that given in the ex9 qustions //
        this function can move any object (Asteroid,Ship,Torpedo) because this three classes
        have the same name of methods that we have set it '''

        new_coord_x = (obj.get_speed_x() + obj.get_place_x() - self.screen_min_x) % \
                      (self.screen_max_x - self.screen_min_x) + self.screen_min_x
        obj.set_place_x(new_coord_x)
        new_coord_y = (obj.get_speed_y() + obj.get_place_y() - self.screen_min_y) % \
                      (self.screen_max_y - self.screen_min_y) + self.screen_min_y
        obj.set_place_y(new_coord_y)

    def set_speed_tor(self,tor,ast,i):

        ''' this function set a torpedo speed by formula we have '''

        sqrt_speeds=math.sqrt((ast.get_speed_x()**2 )+ (ast.get_speed_y()**2))
        new_speed_x=((tor.get_speed_x()+ast.get_speed_x())/(sqrt_speeds))
        new_speed_y = ((tor.get_speed_y() + ast.get_speed_y()) / (sqrt_speeds))
        if i==0:
            tor.set_speed_x(new_speed_x)
            tor.set_speed_y(new_speed_y)
        else:
            tor.set_speed_x((-1)*new_speed_x)
            tor.set_speed_y((-1)*new_speed_y)


    def split_asteroid(self):

        '''  this function its to move torpedo's and check if the torpedo touched the asteroid and split the asteroid
        to asteroid smaller than before and delete the torpedo that touched the asteroid and the torpedo that
        his life ends ! ==200'''


        for tor in self.torp_lst:
            self.move_obj(tor)
            tor.set_life(tor.get_life()+1)
            if tor.get_life()!=TORPEDO_LIFE_LIMIT:
                self._screen.draw_torpedo(tor, tor.get_place_x(), tor.get_place_y(), tor.get_direction())
                for ast in self.ast_lst:
                    if ast.has_intersection(tor):
                        if ast.get_size() == ASTEROID_MIN_SIZE:
                            self.__value += MAX_POINTS
                            self._screen.unregister_asteroid(ast)
                            self.ast_lst.remove(ast)
                            self._screen.unregister_torpedo(tor)
                            self.torp_lst.remove(tor)
                            self._screen.set_score(self.__value)
                            break
                        elif ast.get_size() == ASTEROID_MID_SIZE:
                            self.__value += MID_POINTS
                            for i in range(0, 2):
                                new_ast = Asteroid(ast.get_place_x(),ast.get_place_y(),ASTEROID_MIN_SIZE)
                                self.ast_lst.append(new_ast)
                                self._screen.register_asteroid(new_ast, ASTEROID_MIN_SIZE)
                                self.set_speed_tor(tor,ast,i)
                            self._screen.unregister_asteroid(ast)
                            self.ast_lst.remove(ast)
                            self._screen.unregister_torpedo(tor)
                            self.torp_lst.remove(tor)
                            self._screen.set_score(self.__value)
                            break

                        elif ast.get_size() == ASTEROID_MAX_SIZE:
                            self.__value += MIN_POINTS
                            for i in range(0, 2):
                                new_ast = Asteroid(ast.get_place_x(),ast.get_place_y(),ASTEROID_MID_SIZE)
                                self.ast_lst.append(new_ast)
                                self._screen.register_asteroid(new_ast,ASTEROID_MID_SIZE)
                                self.set_speed_tor(tor, ast, i)
                            self._screen.unregister_asteroid(ast)
                            self.ast_lst.remove(ast)
                            self._screen.unregister_torpedo(tor)
                            self.torp_lst.remove(tor)
                            self._screen.set_score(self.__value)
                            break


            else:
                self._screen.unregister_torpedo(tor)
                self.torp_lst.remove(tor)

    def _game_loop(self):
        '''   Your code goes here!
        this function is moving the ship like the user press
        and make a torpedo's if user press space
        and check if the ship touched the asteroid then give the user message about what happens'''

        self.move_obj(self.ship1)
        if self._screen.is_left_pressed():
            self.ship1.set_direction(LEFT + self.ship1.get_direction())
        if self._screen.is_right_pressed():
            self.ship1.set_direction(RIGHT + self.ship1.get_direction())
        if self._screen.is_up_pressed():
            new_speed_x = self.ship1.get_speed_x() + math.cos(math.radians(self.ship1.get_direction()))
            self.ship1.set_speed_x(new_speed_x)
            new_speed_y = self.ship1.get_speed_y() + math.sin(math.radians(self.ship1.get_direction()))
            self.ship1.set_speed_y(new_speed_y)
        self._screen.draw_ship(self.ship1.get_place_x(), self.ship1.get_place_y(), self.ship1.get_direction())

        if self.ship1.get_life()>0:
            for i in range(0,len(self.ast_lst)):
                if i<len(self.ast_lst):
                    self.move_obj(self.ast_lst[i])
                    if (self.ast_lst[i].has_intersection(self.ship1))==True :
                        self._screen.show_message("ship hits asteroid","your life well decrease")
                        self._screen.remove_life()
                        self.ship1.set_life(self.ship1.get_life()-1)
                        self._screen.unregister_asteroid(self.ast_lst[i])
                        self.ast_lst.remove(self.ast_lst[i])
                    else:
                        self._screen.draw_asteroid(self.ast_lst[i], self.ast_lst[i].get_place_x(),
                                                   self.ast_lst[i].get_place_y())
                else:
                    break

        if len(self.torp_lst)<TORPEDO_LIMIT:
            if self._screen.is_space_pressed():
                new_torpedo = Torpedo(self.ship1.get_place_x(), self.ship1.get_place_y(), self.ship1.get_direction())
                self._screen.register_torpedo(new_torpedo)
                self.torp_lst.append(new_torpedo)
                new_torpedo.set_speed_x(self.ship1.get_speed_x() + 2 * (math.cos(math.radians(new_torpedo.get_direction()))))
                new_torpedo.set_speed_y(
                    self.ship1.get_speed_y() + 2 * (math.sin(math.radians(new_torpedo.get_direction()))))

        self.split_asteroid()

        if len(self.ast_lst)==0:
            self._screen.show_message("NO ASTEROID","you win!!!!")
            self._screen.end_game()
            sys.exit(0)
        if self.ship1.get_life()==0:
            self._screen.show_message("OUT OF LIVES", "you lose!")
            self._screen.end_game()
            sys.exit(0)
        if self._screen.should_end():
            self._screen.show_message("WHY?", "try agin later GOOD BYE!")
            self._screen.end_game()
            sys.exit(0)


def main(amnt):
    runner = GameRunner(amnt)
    runner.run()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int( sys.argv[1] ) )
    else:
        main(DEFAULT_ASTEROIDS_NUM )

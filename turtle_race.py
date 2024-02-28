
from race_window import RaceWindow
from race_turtle import RaceTurtle

class TurtleRace:
    def __init__(self):
        self._w = RaceWindow()
        self._turtles =list()
        self._number_of_turtles=8
        while self._number_of_turtles>0:
            self._turtles.append(RaceTurtle(self._w, self._number_of_turtles))
            self._number_of_turtles-=1                           


    #LEDNING: Så länge det finns turtles kvar i listan som inte gått i mål
    #   loopa över alla Turtles som inte har gått i mål
    #       Låt varje Turtle ta ett race_step
    #       Kolla om den som just tog ett steg kom i mål

            
    def start_race(self) -> None:
        finished_turtles= []
        for turtle in self._turtles:
            while self._turtles:
                if turtle in self._turtles:
                    turtle.race_step()

                    if turtle.xcor() >= self._w.X_END_POS:
                            #turtle = winner #lös detta med winner senare
                            self._turtles.remove(turtle)
                            finished_turtles.append(turtle)
                            print(f'I mål {turtle}')
                        # else:
                        #     turtle.race_step()

    def __str__():
        pass

                    
TurtleRace().start_race()


import turtle
import random

class RaceTurtle(turtle.Turtle):
    #Klass som representerar en sköldpadda som kan springa i ett fönster med racing-banor.

    #Konstruktor:
    def __init__(self, w, nbr):
        super().__init__()
        #Skapar en sköldpadda som ska springa i RaceWindow-objektet w och som har start-nummer nbr. 
        #Sköldpaddan startar med pennan nere och nosen vänd åt höger.
        self._w = w
        self._nbr=nbr
        self._nbr = nbr
        # self.hideturtle()
        self.shape('turtle')
        self.penup()
        self.goto(w.get_start_X(nbr),w.get_start_Y(nbr))
        self.pendown()
        # self.showturtle()

    #Metoder:
    def race_step(self) -> None:
        #Låter sköldpaddan gå framåt ett steg. Stegets längd ges av ett slumptal (heltal) mellan 1 och 6.
        step=random.randint(1,6)
        self.forward(step)

    def __str__(self) -> str:
        #Returnerar en läsbar representation av denna RaceTurtle, på formen "Nummer x" där x är sköldpaddans startnummer.
        return f'Turtle nummer {self._nbr}'

if __name__ == '__main__':
    # w=turtle.mainloop()
    # RaceTurtle(w,1)

    # Create a turtle window
    turtle_screen = turtle.Screen()

    # Create a RaceTurtle and pass the window to it
    race_turtle = RaceTurtle(turtle_screen, 1)

    #testar så att alla steg är olika långa
    colors=['blue', 'red', 'lightgreen', 'yellow']

    for i in range(100):
        race_turtle.pencolor(random.choice(colors))
        race_turtle.race_step()


    print(f'Vinnaren är: {race_turtle}')

    # Keep the window open
    turtle_screen.mainloop() 


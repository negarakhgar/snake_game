from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("my snake game!")
screen.tracer(0)# Turn off automatic updates

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update() # Refresh the screen to show the movement
    time.sleep(1)
    snake.move()




screen.exitonclick()



#segment_2 = Turtle("square")
#segment_2.color("white")
#segment_2.goto(-20,0)



#segment_3 = Turtle("square")
#segment_3.color("white")
#segment_3.goto(-40,0)















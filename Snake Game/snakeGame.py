import turtle 
import time
import random

delay = 0.1

# screen Setting Up
Window = turtle.Screen()
Window.title("Snake Game - Organization Mini Project")
Window.bgcolor("Black")
Window.setup(width=600,height=600)
Window.tracer(0) #turns off the screen updates


# Snake Setting Up
snakeHead = turtle.Turtle()
snakeHead.speed(0)
snakeHead.shape("square")
snakeHead.color("red")
snakeHead.penup()
snakeHead.goto(0,0) 
snakeHead.direction = "stop"


# food
snakeFood = turtle.Turtle()
snakeFood.speed(0)
snakeFood.shape("circle")
snakeFood.color("white")
snakeFood.penup()
snakeFood.goto(0,0) 
snakeFood.direction = "stop"

# list of pieces of our snake
snakeBody = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("Yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align="center", font=('Arial', 20, 'normal'))

score = 0
high_score = 0


# Some helper functions
def go_up():
    if snakeHead.direction != "down":
        snakeHead.direction = "up"

def go_down():
    if snakeHead.direction != "up":
        snakeHead.direction = "down"
    
def go_right():
    if snakeHead.direction != "left":
        snakeHead.direction = "right"
    
def go_left():
    if snakeHead.direction != "right":
        snakeHead.direction = "left"
    
def move():
    if snakeHead.direction == "up":
        snakeHead.sety(snakeHead.ycor()+20)

    if snakeHead.direction == "down":
        snakeHead.sety(snakeHead.ycor()-20)

    if snakeHead.direction == "left":
        snakeHead.setx(snakeHead.xcor()-20)

    if snakeHead.direction == "right":
        snakeHead.setx(snakeHead.xcor()+20)


# keyboard Connections
Window.listen()
Window.onkeypress(go_up,"w")
Window.onkeypress(go_down,"s")
Window.onkeypress(go_left,"a")
Window.onkeypress(go_right,"d")

# main game loop
while True:
    Window.update()
    
    # check for collision with the border
    if snakeHead.xcor()>290 or snakeHead.xcor()<-290 or snakeHead.ycor()>290 or snakeHead.ycor()<-290:
        time.sleep(1.5)
        snakeHead.goto(0,0)
        snakeHead.direction = "stop"
        for piece in snakeBody:
            piece.goto(2000,2000)
        snakeBody.clear()
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=('Arial', 20 , 'normal' ))
        delay = 0.1


    # check for head collision with the food
    if snakeHead.distance(snakeFood) <20: #built-in function to measure the distance between the two objects
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        snakeFood.goto(x,y)
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("grey")
        new_body.penup()
        snakeBody.append(new_body)
        score +=1 #increase score by 1
        if score > high_score: #set high score
            high_score = score
        
        delay -= 0.002 #shorten the delay to make it harder
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=('Arial', 20 , 'normal' ))
    
    # moving the pieces of the snake in a reverse order
    for index in range(len(snakeBody) -1, 0, -1):
        x=snakeBody[index-1].xcor()
        y=snakeBody[index-1].ycor()
        snakeBody[index].goto(x,y)
    
    # moving piece 0 to where the snakeHead is
    if len(snakeBody)>0:
        x = snakeHead.xcor()
        y = snakeHead.ycor()
        snakeBody[0].goto(x,y)

    
    move()
    
    # check for head collision with the body
    for piece in snakeBody:
        if piece.distance(snakeHead)<20:
            time.sleep(1.5)
            snakeHead.goto(0,0)
            snakeHead.direction= "stop"

            for piece in snakeBody:
                piece.goto(2000,2000)
            snakeBody.clear()
            score =0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=('Arial', 20 , 'normal' ))
            delay = 0.1


    time.sleep(delay)
Window.mainloop()
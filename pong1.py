# 1st game
import turtle #gonna build this on top of turtle module lets u do basic graphycs

wn = turtle.Screen() #create a window
wn.title("Pong by sripali")
wn.bgcolor(0.5,0,0.2)
wn.setup(width=800, height=600)
wn.tracer(0) #stops window from updating so we have to manually update it

#Score 
score_a = 0
score_b = 0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation not the speed of paddle set the speed to max possib. speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation not the speed of paddle set the speed to max possib. speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation not the speed of paddle set the speed to max possib. speed
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.04 #ball x movement delta x
ball.dy = -0.04#ball y movement means evey time the ball moves it moves by two pixels

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() #to hide the created turtleitem
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard binding
wn.listen() #lets us listen to keyboard inputs
wn.onkeypress(paddle_a_up, "w")# when w is pressed paddle goes up
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
#main game loop
while True:
    wn.update()
    
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #top and bottom Border check what happen when the ball hit the border
    #screen size is width 800 height 600
    #ball it self is 20*20
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverse the direction
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #reverse the direction 
    #left and right border check
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
    
    #paddle and ball coloosions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *=-1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *=-1
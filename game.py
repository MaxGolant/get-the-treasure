import turtle
import random
import time

rand = random.randint(2,5)

print("loading game...")
time.sleep(rand)

# variables
player = turtle.Turtle()
treasure = turtle.Turtle()
screen = turtle.Screen()
mine1 = turtle.Turtle()
mine2 = turtle.Turtle()
mine3 = turtle.Turtle()
mine4 = turtle.Turtle()
mine5 = turtle.Turtle()
mine6 = turtle.Turtle()
text = turtle.Turtle()
text2 = turtle.Turtle()
cor = random.randint(-300,300)

# settings
player.penup()
player.goto(x = 0, y = -250)
player.color("white")
player.shape("circle")

screen.bgcolor("black")
screen.setup(width = 600, height = 600)
screen.title("Get The Treasure!")

treasure.penup()
treasure.goto(x = 0, y = 250)
treasure.color("gold")
treasure.shape("square")

mine1.goto(x = cor,y = 0)
mine1.ht()

mine2.goto(x = cor,y = 0)
mine2.ht()

mine3.goto(x = cor,y = 0)
mine3.ht()

mine4.goto(x = cor,y = 0)
mine4.ht()

mine5.goto(x = cor,y = 0)
mine5.ht()

mine6.goto(0,0)
mine6.ht()

text.penup()
text.goto(0,0)
text.color("red")
text.hideturtle()
text.speed(0)

text2.penup()
text2.goto(0,0)
text2.color("lightgreen")
text2.hideturtle()

mines = [mine1, mine2, mine3, mine4, mine5, mine6]

# main loop
while True:
    screen.update()
    
    # events
    def up():
        player.setheading(90)
        player.forward(50)

    def down():
        player.setheading(270)
        player.forward(50)

    def right():
        player.setheading(0)
        player.forward(50)

    def left():
        player.setheading(180)
        player.forward(50)

    screen.listen()
    screen.onkey(up, "Up")
    screen.onkey(down, "Down")
    screen.onkey(left, "Left")
    screen.onkey(right, "Right")
    
    if player.distance(mine1) < 50:
        text.goto(0,0)
        text.color("red")
        text.write("Game Over", align = "center", font = ("Courier", 50, "bold"))
        print("You Died")
        time.sleep(100)
        text.color("black")
        treasure.clear()

    if player.distance(mine2) < 50:
        text.goto(0,0)
        text.color("red")
        text.write("Game Over", align = "center", font = ("Courier", 50, "bold"))
        print("You Died")
        time.sleep(100)
        text.color("black")
        treasure.clear()

    if player.distance(mine3) < 50:
        text.goto(0,0)
        text.color("red")
        text.write("Game Over", align = "center", font = ("Courier", 50, "bold"))
        print("You Died")
        time.sleep(100)
        text.color("black")
        treasure.clear()

    if player.distance(mine4) < 50:
        text.goto(0,0)
        text.color("red")
        text.write("Game Over", align = "center", font = ("Courier", 50, "bold"))
        print("You Died")
        time.sleep(100)
        text.color("black")
        treasure.clear()

    if player.distance(mine5) < 50:
        text.goto(0,0)
        text.color("red")
        text.write("Game Over", align = "center", font = ("Courier", 50, "bold"))
        print("You Died")
        time.sleep(100)
        text.color("black")
        treasure.clear()

    if player.distance(mine6) < 50:
        text.goto(0,0)
        text.color("red")
        text.write("Game Over", align = "center", font = ("Courier", 50, "bold"))
        print("You Died")
        time.sleep(100)
        text.color("black")
        treasure.clear()

    if player.distance(treasure) < 20:
        text2.write("Victory!", align = "center", font = ("Courier", 50, "bold"))
        time.sleep(1000)

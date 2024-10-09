import turtle
import time
import random

postpone = 0.1

score = 0
high_score = 0

# window configuration
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# segments / snake body
segments = []

# text
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0,260)
text.write("Score: 0         High Score: 0", align="center", font=("Courier", 20, "normal"))

# functions
def up():
    head.direction = "up"
def down():
    head.direction = "down"
def left():
    head.direction = "left"
def right():
    head.direction = "right"

def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


# Teclado
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

while True:
    wn.update()

    # border colisions
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        [segment.hideturtle() for segment in segments]
        segments.clear()

        # reset
        score = 0
        text.clear()
        text.write("Score: {}         High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))

    # food colisions
    if head.distance(food) < 20:  # el cuadrado y el círculo tienen por defecto 20 píxeles
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        score += 10

        if score > high_score:
            high_score = score

        text.clear()
        text.write("Score: {}         High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))

    # move snake body
    totalSeg = len(segments)
    for index in range(totalSeg - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    mov()

    # body colisions
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(3)
            head.goto(0,0)
            head.direction = "stop"
            [segment.hideturtle() for segment in segments]
            segments.clear()
            
            # reset
            score = 0
            text.clear()
            text.write("Score: {}         High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))

    time.sleep(postpone)
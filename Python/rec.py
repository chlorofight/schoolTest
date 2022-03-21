import turtle

canvas = turtle.Screen()
# canvas.tracer(10)

pen = turtle.Turtle()

# move to the bottom of the screen
pen.penup()
pen.goto(0, -175)
pen.pendown()
pen.speed(0)

# initialize variables
step_size = 0
MAX_STEP = 10
SCALE = 3
numbers_used = []
current = 0

for step_size in range(0, MAX_STEP):
    # go backward if you can
    backward_step = current - step_size
    if backward_step > 0 and backward_step not in numbers_used:
        current = backward_step
        pen.color("red")

    # if you can't go backward, go forward
    else:
        current = current + step_size
        pen.color("black")

    pen.circle(current * SCALE)

    numbers_used.append(current)
5

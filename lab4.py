import turtle
import random

"""PUT YOUR FUNCTIONS HERE"""

def draw_square(t, length):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(90)

def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)


def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)


def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Drawing the stem
    base = radius // 5
    sides = radius // 2
    t.penup()
    t.goto(x + base//2, y + 2*.99*radius)
    t.pendown()

    t.fillcolor("green")
    t.begin_fill()
    t.left(90)  # Point upwards
    t.forward(sides)
    t.left(90)
    t.forward(base)
    t.left(90)
    t.forward(sides)
    t.left(90)
    t.forward(base)
    t.end_fill()

def draw_star(t, x, y, size, color="yellow"):
    """Draws a 5-pointed star at (x, y) with given size and color."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # angle for a star
    t.end_fill()

def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(60)
    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()
    t.left(60)


def drawjackolantern(t, x, y, r):
    draw_pumpkin(t, x, y, r)
    s = .25*r
    # left eye
    draw_eye(t, x - r // 2 + s // 2, y + (2 * r) - r // 1.25, s)
    # right eye
    draw_eye(t, x + r // 2 - s // 2, y + (2 * r) - r // 1.25, s)
    draw_mouth(t, x - r // 2,  y + r//2, r)



def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(50, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
screen = turtle.Screen()
screen.bgcolor("darkblue")
screen.setup(width=600, height=600)
t.clear()



"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""

# Example: draw 10 random stars
"""
for _ in range(10):
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    size = random.randint(15, 50)
    draw_star(t, x, y, size, "yellow")
"""

# Example usage
# draw_circle(t, 50)
# Example usage
#draw_square(t, 100)
# Example usage
#draw_polygon(t, 6, 5)  # Hexagon
# Star in the sky
x = -150
y = -250
r = 100

drawjackolantern(t,x,y,r)
drawjackolantern(t, 0, y, 80)
drawjackolantern(t, -1*x, y-25,r)
# draw_star(t, -100, 150, 30)
# draw_star(t, 100, 180, 20)
draw_sky(t, 30)

screen.exitonclick()








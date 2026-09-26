import turtle
import math
import random
import time

# Advanced Turtle artwork: "Cosmic Bloom"
# Press Space to replay the drawing process.

WIDTH, HEIGHT = 1100, 900
BG = "#07051a"
PALETTE = ["#ff4d8d", "#ff9f1c", "#ffe66d", "#50fa7b", "#38d9ff", "#7c5cff", "#d66efd"]
random.seed(12)

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor(BG)
screen.title("Cosmic Bloom — Advanced Turtle Art")
screen.colormode(255)
screen.tracer(0, 0)

pen = turtle.Turtle(visible=False)
pen.speed(0)
pen.penup()


def pause(seconds=0.35):
    screen.update()
    time.sleep(seconds)


def point(cx, cy, radius, angle):
    radians = math.radians(angle)
    return cx + radius * math.cos(radians), cy + radius * math.sin(radians)


def polygon(cx, cy, radius, sides, color, rotation=0, width=2):
    pen.color(color)
    pen.pensize(width)
    pen.penup()
    x, y = point(cx, cy, radius, rotation)
    pen.goto(x, y)
    pen.pendown()
    for i in range(1, sides + 1):
        x, y = point(cx, cy, radius, rotation + i * 360 / sides)
        pen.goto(x, y)
    pen.penup()


def circle(cx, cy, radius, color, width=2, fill=None):
    pen.color(color)
    pen.pensize(width)
    pen.penup()
    pen.goto(cx, cy - radius)
    pen.setheading(0)
    pen.pendown()
    if fill:
        pen.fillcolor(fill)
        pen.begin_fill()
    pen.circle(radius)
    if fill:
        pen.end_fill()
    pen.penup()


def star(cx, cy, outer, inner, color, points=5, rotation=-90, fill=None):
    pen.color(color)
    pen.pensize(2)
    pen.penup()
    for i in range(points * 2 + 1):
        radius = outer if i % 2 == 0 else inner
        x, y = point(cx, cy, radius, rotation + i * 180 / points)
        if i == 0:
            pen.goto(x, y)
            pen.pendown()
        else:
            pen.goto(x, y)
    pen.penup()
    if fill:
        # Redraw as a filled polygon using turtle's fill state.
        pen.color(color)
        pen.fillcolor(fill)
        pen.penup()
        x, y = point(cx, cy, outer, rotation)
        pen.goto(x, y)
        pen.pendown()
        pen.begin_fill()
        for i in range(1, points * 2 + 1):
            radius = outer if i % 2 == 0 else inner
            pen.goto(*point(cx, cy, radius, rotation + i * 180 / points))
        pen.goto(x, y)
        pen.end_fill()
        pen.penup()


def petal(cx, cy, radius, angle, color):
    # A pointed petal made from two circular arcs.
    pen.color(color)
    pen.pensize(2)
    pen.penup()
    pen.goto(*point(cx, cy, 0, angle))
    pen.setheading(angle + 55)
    pen.pendown()
    pen.circle(radius, 110)
    pen.left(70)
    pen.circle(radius, 110)
    pen.penup()


def orbit(cx, cy, orbit_radius, count, object_radius, colors):
    for i in range(count):
        angle = i * 360 / count
        x, y = point(cx, cy, orbit_radius, angle)
        circle(x, y, object_radius, colors[i % len(colors)], width=2)


def spiral(cx, cy, turns, start_radius, color):
    pen.color(color)
    pen.pensize(2)
    pen.penup()
    pen.goto(cx, cy)
    pen.pendown()
    steps = turns * 180
    for i in range(steps):
        radius = start_radius * i / steps
        angle = i * 2.8
        pen.goto(*point(cx, cy, radius, angle))
    pen.penup()


def background_stars():
    for _ in range(90):
        x = random.randint(-WIDTH // 2 + 15, WIDTH // 2 - 15)
        y = random.randint(-HEIGHT // 2 + 15, HEIGHT // 2 - 15)
        size = random.choice([1, 1, 2, 3])
        circle(x, y, size, random.choice(PALETTE), width=1)
    pause(0.25)


def outer_frame():
    # Layered polygons create a jewel-like frame.
    for radius, sides, color in [(390, 12, "#24166b"), (350, 12, "#4b238f"),
                                  (315, 24, "#8b3dba")]:
        polygon(0, 0, radius, sides, color, rotation=15, width=3)
    for radius in range(280, 100, -30):
        circle(0, 0, radius, PALETTE[(radius // 30) % len(PALETTE)], width=2)
    pause(0.35)


def crystal_rays():
    for i in range(24):
        angle = i * 15
        x, y = point(0, 0, 275, angle)
        star(x, y, 25, 9, PALETTE[i % len(PALETTE)], points=4,
             rotation=angle + 45)
    for orbit_radius, count, size in [(110, 12, 20), (175, 18, 14), (245, 24, 9)]:
        orbit(0, 0, orbit_radius, count, size, PALETTE)
    pause(0.4)


def blooming_core():
    # Twelve large petals surround a layered center.
    for i in range(12):
        petal(0, 0, 115, i * 30, PALETTE[i % len(PALETTE)])
    for radius in range(105, 15, -15):
        circle(0, 0, radius, PALETTE[(radius // 15) % len(PALETTE)], width=3)
    for i in range(16):
        x, y = point(0, 0, 72, i * 22.5)
        circle(x, y, 10, PALETTE[(i + 2) % len(PALETTE)], width=2)
    circle(0, 0, 28, "#fff4a3", width=3, fill="#ffb703")
    circle(0, 0, 10, "#fffde7", width=2, fill="#fffde7")
    pause(0.45)


def comet_spokes():
    # Curving spokes add movement between the core and the frame.
    for i in range(16):
        angle = i * 22.5
        color = PALETTE[i % len(PALETTE)]
        spiral(0, 0, 2, 220, color)
        # Rotate the completed-looking detail with small orbiting stars.
        x, y = point(0, 0, 330, angle)
        star(x, y, 20, 7, color, points=6, rotation=angle)
    pause(0.45)


def finishing_sparkles():
    for i in range(40):
        angle = i * 137.5
        radius = 120 + (i * 19) % 250
        x, y = point(0, 0, radius, angle)
        star(x, y, 5 + i % 5, 1.5, PALETTE[i % len(PALETTE)], points=4,
             rotation=angle + 45)
    pause(0.5)


def draw():
    pen.clear()
    background_stars()
    outer_frame()
    crystal_rays()
    blooming_core()
    comet_spokes()
    finishing_sparkles()
    screen.update()


def replay():
    draw()

screen.onkey(replay, "space")
screen.listen()
draw()
turtle.done()

import turtle

t = turtle.Turtle()
t.speed(100)
t.ht()

width = 1200
height = 600
screen = turtle.Screen()
screen.setup(width, height, 0, 0)

def draw_koch_segment(t, len_segment):
    if len_segment > 6:
        ln = len_segment // 3
        draw_koch_segment(t, ln)
        t.left(60)
        draw_koch_segment(t, ln)
        t.right(120)
        draw_koch_segment(t, ln)
        t.left(60)
        draw_koch_segment(t, ln)
    else:
        t.fd(len_segment)
        t.left(60)
        t.fd(len_segment)
        t.right(120)
        t.fd(len_segment)
        t.left(60)
        t.fd(len_segment)

def draw_sneg_Koch(t, path):
    if path == "right":
        draw_koch_segment(t, 50)
        t.right(120)
        draw_koch_segment(t, 50)
        t.right(120)
        draw_koch_segment(t, 50)
    else:
        draw_koch_segment(t, 50)
        t.left(120)
        draw_koch_segment(t, 50)
        t.left(120)
        draw_koch_segment(t, 50)

draw_sneg_Koch(t, " ")

turtle.done()



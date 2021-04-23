import turtle
import math

class LSystem2D:
    def __init__(self, t, axiom, width, lenght, angle):
        self.axiom = axiom
        self.state = axiom
        self.width = width
        self.lenght = lenght
        self.angle = angle
        self.angle_cumul = 0
        self.fractal_xy = []  # список координат фрактала
        self.posxy = []
        self.rules = {}
        self.t = t
        self.t.pensize(self.width)

    def add_rules(self, *rules):
        for key, value in rules:
            self.rules[key] = value

    def generate_path(self, n_iter):
        for n in range(n_iter):
            for key, value in self.rules.items():
                self.state = self.state.replace(key, value.lower())

            self.state = self.state.upper()

    def set_turtle(self, my_tuple):
        self.t.up()
        self.t.goto(my_tuple[0], my_tuple[1])
        self.t.seth(my_tuple[2])
        self.t.down()

    def draw_turtle(self, start_pos, start_angle):
        turtle.tracer(1, 0)       # Форсажный режим для черепашки
        self.t.up()               # Черепашка перемещается, но не рисет. Поднимается перо
        self.t.setpos(start_pos)  # Стартовая позиция для начала рисования
        self.posxy = start_pos
        self.t.seth(start_angle)  # Стартовый угол поворота
        self.t.down()             # Черепашка опускается и рисует приперемещении
        turtle_stack = []         # Стэк для сохранения предидущих координат черепахи, используется для возврата

        for move in self.state:
            if move == "F":
                self.t.fd(self.lenght)
                alfa = math.radians(self.angle_cumul)  # переводим градусы в радианы
                x = self.posxy[0] + self.lenght * math.sin(alfa)
                y = self.posxy[1] + self.lenght * math.cos(alfa)
                self.posxy = x, y
                self.fractal_xy.append(self.posxy)
                print(len(self.fractal_xy))

            elif move == "S":
                self.t.up()
                self.t.forward(self.lenght)
                alfa = math.radians(self.angle_cumul)  # переводим градусы в радианы


                '''
                self.posxy[0] = self.posxy[0] + self.lenght * math.sin(alfa)
                self.posxy[1] = self.posxy[1] + self.lenght * math.cos(alfa)
                self.fractal_xy.add(self.posxy)
                '''
                self.t.down()
            elif move == "+":
                self.t.left(self.angle)
                self.angle_cumul += angle
            elif move == "-":
                self.t.right(self.angle)
                self.angle_cumul -= angle
            elif move == "[":
                turtle_stack.append((self.t.xcor(), self.t.ycor(), self.t.heading(), self.t.pensize()))
            elif move == "]":
                xcor, ycor, head, w = turtle_stack.pop()
                self.set_turtle((xcor, ycor, head))
                self.width = w
                self.t.pensize(self.width)

        turtle.done()

width = 1200
height = 600
screen = turtle.Screen()
screen.setup(width, height, 0, 0)
t = turtle.Turtle()
t.ht()         # делаем черепашку невидимой

pen_width = 2  # толщина линии рисования
f_len = 10     # длина одного сегмента прямой в пикселах
angle = 25.5    # Фиксированный угол поворота в градусах для ковра Серпинского 60 градусов, для остальных - 90
# axiom = "F+F+F+F"
# axiom = "FX"                # Аксиома для дракона Харвера-Хайтвея
# axiom = "FXF--FF--FF"       # Аксиома для ковра Серпинского
# axiom = "X"                   # Аксиома для кривой Гильберта
# axiom = "A"                      # аксиома для дерева угол 33
axiom = "F"                          # аксиома для дерева 2 и 3 угол 25.7    и 22.5



l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
# l_sys.add_rules(("F", "F+F--F+F"))
# l_sys.add_rules(("F", "F+S-FF+F+FF+FS+FF-S+FF-F-FF-FS-FFF"), ("S", "SSSSSS"))
# l_sys.add_rules(("FX", "FX+FY+"), ("FY", "-FX-FY"))       # Правила для дракона Хартера Хайтвея
# l_sys.add_rules(("F", "FF"), ("X", "--FXF++FXF++FXF--"))    # Правило для ковра Серпинского
# l_sys.add_rules(("X", "-YF+XFX+FY-"), ("Y", "+XF-YFY-FX+"))     # Правило для кривой Гильберта
# l_sys.add_rules(("F", "FF"), ("A", "F[+A][-A]"))                             # Правило для дерева
# l_sys.add_rules(("F", "F[+F]F[-F]F"))                             # Правило для дерева 2 ветка
l_sys.add_rules(("F", "FF-[-F+F+F]+[+F-F-F]"))                             # Правило для дерева 3 сорняк
l_sys.generate_path(2)
l_sys.draw_turtle((0, -200), 90)                              # Для ковра Серпинского стартовый угол ставим -180
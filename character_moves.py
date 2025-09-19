from shutil import move

from pico2d import *

open_canvas()

boy = load_image('character.png')


def move_top():
    print('moving top')
    for x in range(0, 750, 5):
        draw_boy(x, 550)
    pass


def move_right():
    print('moving right')
    for y in range(550, 50, -5):
        draw_boy(750, y)
    pass


def move_bottom():
    print('moving bottom')
    for x in range(750, 50, -5):
        draw_boy(x, 50)
    pass


def move_left():
    print('moving left')
    for y in range(50, 550, 5):
        draw_boy(50, y)

    pass


def move_ractangle():
    print("move rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    
    pass



def move_circle():
    print("move circle")

    r = 200
    for deg in range(0,360):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300

        draw_boy(x, y)
    pass

def move_triangle():
    print("move triangle")
    for x in range(100, 350, 5):
        y = (4/5) * x
        draw_boy(x, y)
    for x in range(350, 650, 5):
        y = (-4/5) * x + 560
        draw_boy(x,y)
    for x in range(650, 100, -5):
        y = 50
        draw_boy(x,y)
    pass

def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


while True:
    # move_circle()
    # move_ractangle()
    move_triangle()

    break
    # pass


close_canvas()

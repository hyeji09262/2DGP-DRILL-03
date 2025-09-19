from pico2d import *
import math

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

def draw_scene(x, y):
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def move_rectangle():
    # 아래쪽(왼->오)
    for x in range(50, 750, 5):
        draw_scene(x, 90)
    # 오른쪽(아래->위)
    for y in range(90, 550, 5):
        draw_scene(750, y)
    # 위쪽(오->왼)
    for x in range(750, 50, -5):
        draw_scene(x, 550)
    # 왼쪽(위->아래)
    for y in range(550, 90, -5):
        draw_scene(50, y)

def move_circle():
    cx, cy, r = 400, 300, 210
    for deg in range(0, 360, 2):
        rad = math.radians(deg)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        draw_scene(x, y)

while True:
    move_rectangle()
    move_circle()

close_canvas()


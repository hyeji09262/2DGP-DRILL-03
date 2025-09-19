from pico2d import *
import math

open_canvas()

boy = load_image('character.png')

def draw_boy(x: float, y: float):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.01)

def move_rectangle():
    # 상단 이동 (왼쪽 -> 오른쪽)
    for x in range(50, 750, 5):
        draw_boy(x, 550)
    # 우측 이동 (위 -> 아래)
    for y in range(550, 50, -5):
        draw_boy(750, y)
    # 하단 이동 (오른쪽 -> 왼쪽)
    for x in range(750, 50, -5):
        draw_boy(x, 50)
    # 좌측 이동 (아래 -> 위)
    for y in range(50, 550, 5):
        draw_boy(50, y)

def move_circle():
    r = 200
    cx, cy = 400, 300
    for deg in range(0, 360, 2):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        draw_boy(x, y)

while True:
    move_rectangle()
    move_circle()
    break

close_canvas()


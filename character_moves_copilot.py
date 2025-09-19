from pico2d import *
import math

open_canvas()

boy = load_image('character.png')

def draw_boy(x: float, y: float):
    clear_canvas_now()
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

def move_triangle():
    # 삼각형의 세 꼭짓점 좌표
    x1, y1 = 400, 550  # 위쪽 꼭짓점
    x2, y2 = 750, 90   # 오른쪽 아래 꼭짓점
    x3, y3 = 50, 90    # 왼쪽 아래 꼭짓점

    # 1. (x1, y1) -> (x2, y2)
    for t in range(0, 101):
        x = x1 + (x2 - x1) * t / 100
        y = y1 + (y2 - y1) * t / 100
        draw_boy(x, y)
    # 2. (x2, y2) -> (x3, y3)
    for t in range(0, 101):
        x = x2 + (x3 - x2) * t / 100
        y = y2 + (y3 - y2) * t / 100
        draw_boy(x, y)
    # 3. (x3, y3) -> (x1, y1)
    for t in range(0, 101):
        x = x3 + (x1 - x3) * t / 100
        y = y3 + (y1 - y3) * t / 100
        draw_boy(x, y)

while True:
    move_rectangle()
    move_circle()
    move_triangle()

close_canvas()

#COMP 1020 Assignment by Beomsu Kim

from graphics import *

def draw_fun_shape(x, y, win):
    body = Rectangle(Point(x - 15, y - 40), Point(x + 15, y + 40))
    body.setFill("silver")
    body.setOutline("black")
    body.draw(win)

    window = Circle(Point(x, y - 10), 10)
    window.setFill("skyblue")
    window.setOutline("black")
    window.draw(win)

    nose = Polygon(Point(x - 15, y - 40), Point(x + 15, y - 40), Point(x, y - 70))
    nose.setFill("red")
    nose.setOutline("black")
    nose.draw(win)

    left_fin = Polygon(Point(x - 15, y + 40), Point(x - 35, y + 60), Point(x - 15, y + 60))
    left_fin.setFill("orange")
    left_fin.draw(win)

    right_fin = Polygon(Point(x + 15, y + 40), Point(x + 35, y + 60), Point(x + 15, y + 60))
    right_fin.setFill("orange")
    right_fin.draw(win)

    flame = Polygon(Point(x - 10, y + 40), Point(x + 10, y + 40), Point(x, y + 80))
    flame.setFill("yellow")
    flame.draw(win)

def clear_window(win):
    bg = Rectangle(Point(0, 0), Point(win.getWidth(), win.getHeight()))
    bg.setFill("black")
    bg.setOutline("black")
    bg.draw(win)

def main():
    win = GraphWin("Animate Shape", 600, 400)
    win.setBackground("black")

    while True:
        clear_window(win)
        mouse_point = win.getMousePosition()
        x = mouse_point.getX()
        y = mouse_point.getY()
        draw_fun_shape(x, y, win)
        update()

if __name__ == "__main__":
    main()

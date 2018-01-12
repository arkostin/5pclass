#!/usr/bin/python3
from graphics import *
def main():
	win = GraphWin()
	c = Circle(Point(100,100),50)
	c.draw(win)
	win.getMouse()
	win.close()
main()

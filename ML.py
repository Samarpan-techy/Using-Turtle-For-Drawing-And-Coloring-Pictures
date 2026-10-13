import cv2
import numpy as np
import turtle
img_pat='bholenath.jpg'
image=cv2.imread(img_pat)
if image is None:
    print("Sorry")
    exit()
width,h=120,120
img = cv2.resize(image,(width,h))
screen=turtle.Screen()
screen_w,screen_h=600,600
screen.setup(screen_w,screen_h)
screen.title("mata rani")
screen.bgcolor("white")
artist=turtle.Turtle()
artist.speed(0)
artist.penup()
screen.tracer(50000000,0)
print("Jai Mata Di")
for y in range(h):
    for i in range(width):
        b,g,r=img[y,i]
        col=(r/255.0,g/255.0,b/255.0)
        scale_x= screen_w//width
        scale_r=screen_h//h
        screen_x=(i-width//2)*scale_x
        screen_y=(h//2-y)*3
        artist.goto(screen_x,screen_y)
        artist.dot(scale_x+1,col)
        screen.update()
print("JMD")
turtle.done()


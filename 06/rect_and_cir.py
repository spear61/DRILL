import math
from pico2d import *

open_canvas()
#800, 600

def printCHR():
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    

grass = load_image('grass.png')
character = load_image('character.png')
x=400
y=90
c=0

while(1):    
        for i in range(400,800):
            printCHR()
            x=i
            delay(0.01)            
        for i in range(90,600):
            printCHR()
            y=i
            delay(0.01)            
        for i in range(800,0,-1):
            printCHR()
            x=i
            delay(0.01)           
        for i in range(600,90,-1):
            printCHR()
            y=i
            delay(0.01)           
        for i in range(0,400):
            printCHR()
            x=i
            delay(0.01)
            
    
        



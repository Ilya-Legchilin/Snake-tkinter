from tkinter import *
import random
import math

root = Tk()
root.title('Змейка')
root.geometry('600x400')
root['bg'] = '#000000'
root.resizable(width=False, height=False)


UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"


class Snake():
    def __init__(self, x1, y1, x2, y2):
        if x1 != x2:
            self.length = abs(x1 - x2) + 1
            if x1 > x2:
                self.direction = RIGHT
            else:
                self.direction = LEFT
        else:
            self.length = abs(y1 - y2) + 1
            if y1 > y2:
                self.direction = UP
            else:
                self.direction = DOWN
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.position = []
        if x1 == x2:
            for i in range(self.length):
                self.position.append((x1, y1 - i))
        else:
            for i in range(self.length):
                self.position.append((x1 - i, y1))
        
        
    def move(self):
        new_position = [None]*self.length
        if self.direction == UP:
            new_position[0] = (self.position[0][0], self.position[0][1] + 1)
        elif self.direction == DOWN:
            new_position[0] = (self.position[0][0], self.position[0][1] - 1)
        elif self.direction == RIGHT:
            new_position[0] = (self.position[0][0] + 1, self.position[0][1])
        elif self.direction == LEFT:
            new_position[0] = (self.position[0][0] - 1, self.position[0][1])
        for i in range(1, self.length):
                new_position[i] = self.position[i-1]
        self.position = new_position
        
     
    def set_direction(self, direction):
        if self.direction == UP and direction == DOWN:
            return
        elif self.direction == DOWN and direction == UP:
            return
        elif self.direction == RIGHT and direction == LEFT:
            return
        elif self.direction == LEFT and direction == RIGHT:
            return
        else:
            self.direction = direction


def spawn_snake():
    pass


def spawn_apple():
    pass  


snake = Snake(2, 5, 2, 1)
snake.set_direction(RIGHT)

c_list = []

for i in range(20):
    for j in range(30):
        c = Canvas(root, bg='white', width=14, height=14)
        c.grid(row=i, column=j, pady=1, padx=1)
        c_list.append(c)
            

def paint_cell(i, j, color):
    index = i*30 + j
    a = c_list[index]
    a.config(bg=color)
    

for i in range(snake.length):
    a = snake.position[i][0]
    b = snake.position[i][1]
    paint_cell(b, a, 'grey')
    
def update():
    empty = Label(root)
    for i in range(snake.length):
        a = snake.position[i][0]
        b = snake.position[i][1]
        paint_cell(b, a, 'white')
    snake.move()
    for i in range(snake.length):
        a = snake.position[i][0]
        b = snake.position[i][1]
        paint_cell(b, a, 'grey')
    empty.after(500, update)
    
update()
    


root.mainloop()
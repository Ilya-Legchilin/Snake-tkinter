from tkinter import *
from tkinter import messagebox as mb
import random
import math

root = Tk()
root.title('Змейка')
root.geometry('300x200')
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
                self.direction = UP
            else:
                self.direction = DOWN
        else:
            self.length = abs(y1 - y2) + 1
            if y1 > y2:
                self.direction = LEFT
            else:
                self.direction = RIGHT
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
            if self.position[0][1] == 9:
                return "Game over"
            new_position[0] = (self.position[0][0], self.position[0][1] + 1)
        elif self.direction == DOWN:
            if self.position[0][1] == 0:
                return "Game over"
            new_position[0] = (self.position[0][0], self.position[0][1] - 1)
        elif self.direction == RIGHT:
            if self.position[0][0] == 14:
                return "Game over"
            new_position[0] = (self.position[0][0] + 1, self.position[0][1])
        elif self.direction == LEFT:
            if self.position[0][0] == 0:
                return "Game over"
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
    x1 = random.randint(4, 12)
    y1 = random.randint(4, 7)
    if random.randint(0, 50) % 2 == 0:
        x2 = x1 + 2
        y2 = y1
    else:
        x2 = x1
        y2 = y1 + 2
    snake = Snake(x1, y1, x2, y2)
    print(snake.direction)
    return snake
    

    
    
snake = spawn_snake()    
    
    
class Apple():
    def __init__(self):
        self.x = random.randint(1, 14)
        self.y = random.randint(1, 9)
        for i in range(snake.length):
            if (self.x, self.y) == snake.position[i]:
                self.respawn()
        
    
    def respawn(self):
        self.x = random.randint(1, 14)
        self.y = random.randint(1, 9)
        for i in range(snake.length - 1):
            if (self.x, self.y) == snake.position[i]:
                self.respawn()


apple = Apple()

c_list = []

for i in range(10):
    for j in range(15):
        c = Canvas(root, bg='white', width=14, height=14)
        c.grid(row=i, column=j, pady=1, padx=1)
        c_list.append(c)
            

def paint_cell(i, j, color):
    index = i*15 + j
    a = c_list[index]
    a.config(bg=color)
    

for i in range(snake.length):
    a = snake.position[i][0]
    b = snake.position[i][1]
    paint_cell(b, a, 'grey')
    
def update():
    empty = Label(root)
    
    paint_cell(apple.y, apple.x, 'red')
    
    for i in range(snake.length):
        a = snake.position[i][0]
        b = snake.position[i][1]
        paint_cell(b, a, 'white')
    if snake.position[0][0] == apple.x and snake.position[0][1] == apple.y:
        snake.length += 1
        paint_cell(apple.y, apple.x, 'white')
        apple.respawn()
        paint_cell(apple.y, apple.x, 'red')
    if snake.move() == "Game over":
        mb.showinfo(message="Game over!")
        root.destroy()
    for i in range(snake.length):
        a = snake.position[i][0]
        b = snake.position[i][1]
        paint_cell(b, a, 'grey')
    for i in range(1, snake.length):
        if snake.position[0] == snake.position[i]:
            mb.showinfo(message="Game over!")
            root.destroy()
    
            
    empty.after(300, update)

    
def key_up(event): 
    snake.set_direction(UP)
    
 
def key_down(event): 
    snake.set_direction(DOWN)
    
    
def key_right(event): 
    snake.set_direction(RIGHT)
    
    
def key_left(event): 
    snake.set_direction(LEFT)
    
    
root.bind('<Up>', key_down)
root.bind('<Left>', key_left)
root.bind('<Down>', key_up)    
root.bind('<Right>', key_right)    
update()
    


root.mainloop()
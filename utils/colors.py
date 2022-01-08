#!/bin/env python3
from sys import argv, stdin
from random import randint

class fg_color():
    def __init__(self) -> None:
        self.r, self.g, self.b = int, int, int
        self.gen_fg_rgb()
    
    def gen_fg_rgb(self):
        self.r, self.g, self.b = randint(0, 255), randint(0, 255), randint(0, 255)

    def put_color(self, text):
        text = f"\u001b[38;2;{self.r};{self.g};{self.b}m{text}"
        text += "\u001b[0m"
        return text
    
    
def fg_rgb(text):
    r,g,b = randint(0, 255), randint(0, 255), randint(0, 255)
    text = f"\u001b[38;2;{r};{g};{b}m{text}"
    text += "\u001b[0m"
    return text

# def bg_rgb(text):
#     colors = "black": "\u001b[40m" + text + "\u001b[0m", # 40-47m
#         return f"\u001b[48;2;{r};{g};{b}m{text}

    

# pipe_line
# color = fg_color()
# for n in stdin.readlines():
#     n = n.strip('\n')
#     print(color.put_color(n))

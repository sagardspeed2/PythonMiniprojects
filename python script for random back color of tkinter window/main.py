from tkinter import *
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500,500))

class App:

    def __init__(self):

        self.root = Tk()
        self.root.title("ranfom background change")
        self.root.geometry("100x100+800+10")
        Button(self.root, text="random", command=self.set_random).pack()


    def set_random(self):

        screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


app = App()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            quit()


    pygame.display.update()

    if running:

        app.root.update()
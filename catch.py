import pgzrun
import random

WIDTH = 600
HEIGHT = 600

score = 0

# fruits pos
apple = Actor('apple')
apple.pos = 100, 100

orange = Actor('orange')
orange.pos = 200, 100

grapes = Actor('grapes')
grapes.pos = 300, 100

banana = Actor('banana')  
banana.pos = 400, 100

fruits = [apple, orange, grapes, banana]

# Basket pos
basket = Actor('basket')
basket.pos = 300, 550

def draw():
    screen.clear()
    for fruit in fruits:
        fruit.draw()
    basket.draw()
    screen.draw.text("Score: " + str(score), topleft=(10, 10), fontsize=40, color="black")

def update():
    global score

    for fruit in fruits:
        fruit.y += 1
        if fruit.colliderect(basket):
            score += 1                      
# '''remove the fruit and collition of basket And Use clock.schedule_interval function to create fruits on every 2 or 3 seconds
# '''

    # basket move
    if keyboard.left:
        basket.x -= 5
    elif keyboard.right:
        basket.x += 5

pgzrun.go()









pgzrun.go()

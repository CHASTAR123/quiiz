import pgzrun

TITLE = "quiz master"
WIDTH = 600
HEIGHT = 600

options = []

marqueebox = Rect(0, 0, WIDTH, 100)
questionbox = Rect(10, 100, 400, 200)

#option boxes pos
for i in range(2):
    option = Rect(0, 0, 250, 100)
    option.move_ip(10, 320 + i * 120) 
    options.append(option)

timer = Rect(420, 100, 80, 200)
skipbox = Rect(420, 300, 80, 200)

def draw():
    screen.clear()
     # marquee
    screen.draw.rect(marqueebox, 'yellow')
    screen.draw.text("Quiz Master", center=marqueebox.center, fontsize=40, color="black")
    # q.uestion box
    screen.draw.rect(questionbox, 'white')
    screen.draw.text("Question goes here", center=questionbox.center, color="black")

pgzrun.go()
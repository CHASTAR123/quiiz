import pgzrun,time

TITLE = "quiz master"

WIDTH = 600
HEIGHT = 600

options = []

marqueebox = Rect(0,0,WIDTH,100) 
questionbox = Rect(0,0,500,200) 
"""

for i in range(4):
    option1 = Rect(0,0,200,100) 
    options.append(option1)
"""
timerbox = Rect(0,0,80,200)
skipbox = Rect(0,0,80,200)

marqueebox.move_ip(0,0)
questionbox.move_ip(10,120)
timerbox.move_ip(520,120)
skipbox.move_ip(520,340)

option1 = Rect(0,0,245,100) 
option2 = Rect(0,0,245,100) 
option3 = Rect(0,0,245,100) 
option4 = Rect(0,0,245,100) 

option1.move_ip(10,340)
option2.move_ip(265,340)
option3.move_ip(10,460)
option4.move_ip(265,460)
options = [option1,option2,option3,option4]

score = 0
timer = 10
message = ''
game_over = False
questions = []
question_count,question_index = 0,0

def draw():    
    screen.fill('yellow')
    # screen.clear()
    screen.draw.filled_rect(marqueebox,'light blue')
    screen.draw.filled_rect(questionbox,'red')
    for i in options:
        print(i)
        screen.draw.filled_rect(i,'blue')
        
    screen.draw.filled_rect(timerbox,'green')
    screen.draw.filled_rect(skipbox,'orange')


def read_que_file():
    global questions,question_count
    file = open('pgzero\questions.txt',"r")
    for i in file:
        questions.append(i)
        question_count += 1
    print(questions)
    file.close()

def read_next_que():
    global question_index
    question_index += 1
    return questions.pop(0).split(',')
def update_timer():
    global timer
    if timer:
        timer -= 1
    else:
        gameover()

def on_mouse_down(pos):
    global score, timer, question
    index = 1
    for i in options:
        if i.collidepoint(pos):
            if index is int(question[5]):
                score += 1
                if questions:
                    question = read_next_que()
                    timer = 10
                else:
                    game_over()
            else:
                game_over()     
        index += 1   
    if skipbox.collidepoint(pos):
        if questions:
            question = read_next_que()
            timer = 10
        else:
            game_over()


    

read_que_file()
question = read_next_que()
print(question)
clock.schedule_interval(update_timer,1)




pgzrun.go()








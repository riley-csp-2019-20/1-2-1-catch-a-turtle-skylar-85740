# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl 
import random as rand
import turtle as trtl

#-----game configuration----
fruit = trtl.Turtle()
fruit.shape("circle")
fruit.shapesize(4)
fruit.fillcolor("red")
fruit.speed(6)
score = 0
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(0,-300)
score_writer.pendown()
score_writer.speed(4)
#-----countdown writer-----
counter =  trtl.Turtle()
counter.penup()
counter.goto(0,300)
counter.pendown()

#-----initialize turtle-----

#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 10
counter_interval = 1000   #1000 represents 1 second
timer_up = False


#-----game functions--------
def fruit_clicked(x, y):
    change_position()   
    update_score() 
    countdown()
    score_writer.write(score, font=font_setup)
        
def change_position():
    fruit.penup()
    fruit.hideturtle()
    if not timer_up:
      fruitx = rand.randint(-400,400)
      fruity = rand.randint(-200,200)
      fruit.goto(fruitx,fruity)
      fruit.st()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    print(score)
    
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 






#-----events----------------
fruit.onclick(fruit_clicked)



wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()

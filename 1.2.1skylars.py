# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl 
import random as rand



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

#-----initialize turtle-----



#-----game functions--------
def fruit_clicked(x, y):
    change_position()   
    update_score() 
    score_writer.write(score, font=font_setup)

def change_position():
    fruit.penup()
    fruit.hideturtle()
    new_xcor = rand.randint(-400, 400)
    new_ycor = rand.randint(-200, 300)
    fruit.goto(new_xcor, new_ycor)
    fruit.pendown()
    fruit.showturtle()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    print(score)
    

def font_setup():
    ("Arial", 20, "normal")




#-----events----------------
fruit.onclick(fruit_clicked)



wn = trtl.Screen()
wn.mainloop()

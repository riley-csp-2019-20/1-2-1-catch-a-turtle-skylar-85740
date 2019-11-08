# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl 
import random as rand



#-----game configuration----
fruit = trtl.Turtle()
fruit.shape("circle")
fruit.shapesize(4)
fruit.fillcolor("red")
fruit.speed(4)

#-----initialize turtle-----



#-----game functions--------
def fruit_clicked(x, y):
    change_position()    

def change_position():
    fruit.penup()
    fruit.hideturtle()
    new_xcor = rand.randint(-400, 400)
    new_ycor = rand.randint(-300, 300)
    fruit.goto(new_xcor, new_ycor)
    fruit.pendown()
    fruit.showturtle()




#-----events----------------
fruit.onclick(fruit_clicked)

    




wn = trtl.Screen()
wn.mainloop()

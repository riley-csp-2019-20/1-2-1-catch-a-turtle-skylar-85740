# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl 
fruit = trtl.Turtle()


#-----game configuration----
fruit.shape("circle")
fruit.shapesize(4)
fruit.fillcolor("red")

#-----initialize turtle-----
def fruit_clicked(x, y):
    change_position()    

#-----game functions--------


#-----events----------------
fruit.onclick(fruit_clicked)
import random as rand
fruit_x = fruit.xcor()
fruit_y = fruit.ycor()
def change_position():
    rand.randint(x,y)
    new_xpos()
    new_ypos()




wn = trtl.Screen()
wn.mainloop()
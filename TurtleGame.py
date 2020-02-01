import turtle
import sys
import random
import math
import os
import time

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Python Game")


turtle.register_shape("enemy.gif")

 
player=turtle.Turtle()
player.color("red")
player.shape("turtle")
player.up()
player.speed(0)  #Animation Speed not the Turtle speed



wall=turtle.Turtle()
wall.color("green")
wall.up()
wall.setposition(-300,-300)
wall.hideturtle()
wall.down()
wall.pensize(3)
for side in range(4):
    wall.speed(7)
    wall.fd(600)
    wall.left(90)

wall.color("white")


speed=8
Score = 0       


def turnleft():
    player.left(90)
    global speed
    if speed>10 and speed<15:
        speed+=0.5

def turnright():
    player.right(90)
    global speed
    if speed>10 and speed<15:
        speed+=0.5

def increasespeed():
    global speed
    player.forward(speed)
    speed+=1.5

def decreasespeed():
    global speed
    if speed>=3:
        speed-=1


def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<20:
        return True
    else:
        return False

def follow_runner():
    enemy.setheading(enemy.towards(player))
    enemy.forward(7)
    wn.ontimer(follow_runner, 1)    



turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")
turtle.onkey(decreasespeed,"Down")


goal=turtle.Turtle()
goal.color("yellow")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(random.randint(-280,280),random.randint(-280,280))


score=turtle.Turtle()
score.penup()
score.setpos(350,250)
score.color("white")
score.write('Score : ', font=("Arial", 16, "bold"))
score.setpos(435,252)
score.ht()



os.chdir(r'F:\Projects\Python Projects\TurtleGame') #Write the path of this file where you put it.Put it within the quotes .
f = open("Turtlegame.txt",'r')# Put this file also in the same folder as TurtleGame.py is in
value = int(f.read())



highscore=turtle.Turtle()
highscore.penup()
highscore.setpos(350,220)
highscore.color("white")
highscore.write('High Score : ', font=("Arial", 16, "bold"))
highscore.setpos(480,220)
highscore.ht()


enemies = []

for i in range(7):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("blue")
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-280,280)
    y = random.randint(-280,280)
    enemy.setposition(x,y)
    


    
enemyspeed = 7


    


while True:
    player.forward(speed)

    for enemy in enemies:
        
        #enemy.forward(enemyspeed)

        enemy.forward(enemyspeed)
        #follow_runner()
        
        if enemy.xcor()>280 or enemy.xcor()<-280:
            enemy.right(180)
            
        if enemy.ycor()>280 or enemy.ycor()<-280:
            enemy.left(180)

        if isCollision(enemy,player):
                time.sleep(0.5)
                print("GAME OVER")
                print("\n")
                print("Your Score: ",Score)
                print("High Score: ",end="")



                f = open('Turtlegame.txt','r')

                value_as_int = int(f.read())

                if Score > value_as_int:
                      f = open('Turtlegame.txt','w')
                      f.write(str(Score))
                      f.close()

                f = open('Turtlegame.txt','r')
                print(f.read())



                wn.delay(10)
                os._exit(0)

        
                
    if player.xcor()>280 or player.xcor()<-280:
            break;
    if player.ycor()>280 or player.ycor()<-280:
            break;
    
    
    


    
    if isCollision(player,goal):
        Score+=5
        goal.setposition(random.randint(-280,280),random.randint(-280,280))
        
        if speed<10:
            speed+=1
                 
                
        

    if Score!=0:
        score.undo()
        score.ht()
        score.write(Score,align="left",font=("Arial",14,"normal"))     
        

    if Score > value:
        value+=5

    else:
        highscore.undo()
        highscore.ht()
        highscore.write(value,align="left",font=("Arial",14,"normal"))
                
    


        
           
time.sleep(0.5)
print("GAME OVER")
print("\n")
print("Your Score: ",Score)
print("High Score: ",end="")



f = open('Turtlegame.txt','r')

value_as_int = int(f.read())

if Score > value_as_int:
      f = open('Turtlegame.txt','w') # Text File to store HighScore
      f.write(str(Score))
      f.close()

f = open('Turtlegame.txt','r')
print(f.read())



wn.delay(10)
wn.bye()

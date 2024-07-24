import turtle as t

t.speed(50)

up = t.penup
down = t.pendown
c = t.circle
pos = t.setpos

t.title("Olimpia")

#kék kör
t.pensize(5)
t.color("blue")
up()
pos(-150, 50)
down()
c(45, -330)

up()

#fekete kör
t.color("black")
pos(-30, 55)
down()
c(45, 250)
up()
c(45, 30)
down()
c(45, 50)

up()

#piros kör
t.color("red")
pos(45, 50)
down()
c(45, 270)
up()
c(45, 30)
down()
c(45, 60)

up()

#sárga kör
t.color("yellow")
pos(-105, -10)
down()
c(45, 90)
up()
c(45, 30)
down()
c(45, 45)
up()
c(45, 30)
down()
c(45, 165)

up()

#zöld kör
t.color("green")
pos(-4, -8)
down()
c(45, 90)
up()
c(45, 30)
down()
c(45, 45)
up()
c(45, 30)
down()
c(45, 165)

up()

#szöveg
pos(-150, -75)
t.color("magenta")
t.write("Paris 2024", font=("Comic Sans MS", 24, "normal"))

t.hideturtle()

t.exitonclick()
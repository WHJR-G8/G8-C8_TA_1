import turtle

n1 = int(input('Enter the no of the sides of the polygon : '))
l1 = int(input('Enter the length of the sides of the polygon : '))

def draw_polygon(n,l):
    for _ in range(n):
        turtle.forward(l)
        turtle.right(360 / n)

draw_polygon(n1, l1)

n2 = int(input('Enter the no of the sides of the polygon : '))
l2 = int(input('Enter the length of the sides of the polygon : '))

turtle.penup()
turtle.goto(80, 40)
turtle.pendown()

draw_polygon(n2, l2)

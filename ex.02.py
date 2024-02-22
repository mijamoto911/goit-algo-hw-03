'''«сніжинка Коха»'''


import turtle

def koch_snowflake(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        koch_snowflake(order-1, size/3)
        turtle.left(60)
        koch_snowflake(order-1, size/3)
        turtle.right(120)
        koch_snowflake(order-1, size/3)
        turtle.left(60)
        koch_snowflake(order-1, size/3)

turtle.speed(0)
turtle.penup()
turtle.goto(-150, 90)
turtle.pendown()
turtle.ht()

for i in range(3):
    koch_snowflake(4, 300)
    turtle.right(120)
turtle.done()
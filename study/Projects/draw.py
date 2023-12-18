import turtle

ws= turtle.Turtle()
ws.speed(0)
ws.color("blue")

for j in range(1,100):
    for i in range(1,9):
        ws.left(10)
        ws.right(67)
        ws.forward(100)
    ws.left(5)
    for j in range(1,100):
        for i in range(1,9):
            ws.left(10)
            ws.right(700)
            ws.forward(100)
    ws.left(5)
turtle.done()
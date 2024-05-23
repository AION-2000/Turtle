import turtle

turtle.bgcolor('black')
t = turtle.Turtle()
colors = ['red', 'blue']  # Choose your color

try:
    for number in range(400):
        t.forward(number + 1)
        t.right(89)
        t.pencolor(colors[number % 2])
except turtle.Terminator:
    print("Turtle graphics window was closed. Exiting gracefully.")
finally:
    turtle.done()

import turtle

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=750, height=500)
wn.tracer(0)

# main loop
while True:
    wn.update()
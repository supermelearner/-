import turtle as t
k=40
#
def draw(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range (4):
        t.fd(k)
        t.right(90)
    t.end_fill()
sk=5
t.tracer(False)
for i in range (8):
    y=160-i*40
    sk-=2*sk
    for j in range (8):
        sk-=2*sk
        x=-160+j*40
        if (sk>0):
            t.color('black','white')
            draw(x,y)
        if (sk<0):
            t.color('black','black')
            draw(x,y)
            

t.tracer(True)

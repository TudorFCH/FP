import turtle

t = turtle.Pen()
def menu():

    return"""
            1 - zeichne rechtecke
            2 - zeichne hertz
            3 - zeichne hauser
            0 - exit
            """

def main():

    while True:
        print(menu())
        opt = int(input('opt= '))

        if opt == 1:
            rechtecke()

        if opt == 2:
            hertz()

        if opt == 3:
            hauser()

        if opt == 0:
            break

def rechtecke():
    t.up()
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.down()
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.up()
    t.forward(75)
    t.right(90)
    t.forward(37.5)
    t.down()
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.reset()

def hertz():
    t.left(120)
    t.right(180)
    t.forward(20)
    t.left(180)
    t.forward(200)
    for n in range(180):
        t.right(1)
        t.forward(1)
    t.left(120)
    for n in range(180):
        t.right(1)
        t.forward(1)
    t.forward(200)
    t.reset()

def hauser():
    t.up()
    t.forward(100)
    t.down()

    #wande

    t.forward(100)
    t.left(180)
    t.up()
    t.forward(200)
    t.down()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.up()
    t.forward(100)
    t.down()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.up()
    t.right(90)
    t.forward(100)
    t.right(90)
    t.down()
    t.forward(100)
    t.left(90)
    t.up()
    t.forward(100)
    t.left(90)
    t.down()
    t.forward(100)
    t.right(90)

    #ende wande
    #tur und fenster 1

    t.forward(35)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(10)
    t.up()
    t.left(90)
    t.forward(25)
    t.down()
    t.left(90)
    t.forward(5)
    t.right(90)
    t.forward(2)
    t.right(180)
    t.up()
    t.forward(27)
    t.left(90)
    t.forward(5)
    t.down()
    t.forward(20)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.up()
    t.right(90)
    t.forward(60)
    t.down()
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(180)
    t.forward(15)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.up()
    t.forward(15)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.down()
    t.forward(30)
    t.left(90)
    t.up()

    #ende tur und fenster 1

    t.forward(75)
    t.left(90)
    t.forward(265)
    t.left(180)
    t.down()

    #tur und fenster 2

    t.forward(35)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(10)
    t.up()
    t.left(90)
    t.forward(25)
    t.down()
    t.left(90)
    t.forward(5)
    t.right(90)
    t.forward(2)
    t.right(180)
    t.up()
    t.forward(27)
    t.left(90)
    t.forward(5)
    t.down()
    t.forward(20)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.up()
    t.right(90)
    t.forward(60)
    t.down()
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(180)
    t.forward(15)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.up()
    t.forward(15)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.down()
    t.forward(30)
    t.left(90)
    t.up()

    #ende tur und fenster 2

    t.right(180)
    t.forward(25)
    t.left(90)
    t.forward(235)
    t.down()

    #dach 1

    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.up()

    #dach 2

    t.left(60)
    t.forward(100)
    t.down()
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.reset()

main()
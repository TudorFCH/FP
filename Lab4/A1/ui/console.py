import turtle
from logik.letters import draw_a,draw_b,draw_c,draw_d,draw_e,draw_f,draw_g,draw_h,draw_i,draw_j,draw_k
from logik.letters import draw_l,draw_m,draw_n,draw_o,draw_p,draw_q,draw_r,draw_s,draw_t,draw_u,draw_v
from logik.letters import draw_w,draw_x,draw_y,draw_z,draw_dot,draw_exclam,draw_question

from logik.instructions import w,s,d,a,f,g

def user_input():

    d = {"a": draw_a, "b": draw_b, "c": draw_c, "d": draw_d, "e": draw_e, "f": draw_f, "g": draw_g,
         "h": draw_h, "i": draw_i, "j": draw_j, "k": draw_k, "l": draw_l, "m": draw_m, "n": draw_n,
         "o": draw_o, "p": draw_p, "q": draw_q, "r": draw_r, "s": draw_s, "t": draw_t, "u": draw_u,
         "v": draw_v, "w": draw_w, "x": draw_x, "y": draw_y, "z": draw_z, ".": draw_dot, "!": draw_exclam,
         "?":draw_question}

    text=input('Your input is:')
    l=list(text)
    shift=0

    wn = turtle.Screen()
    for i in range(len(l)):
        if l[i]==' ':
            shift+=50
        else:
            d[l[i]](shift)
            shift+=40


    wn.exitonclick()




def user_input1():
    inputs = []
    ok=1
    dict = {"w": w, "s": s, "d": d, "a": a, "f": f, "g": g}

    str = input('your input is:')

    for i in range(len(inputs)):
        if inputs[i]==str:
            ok=0

    if ok==0:
        print('Es gibt dieses Zeichen schon')
    else:
        inputs += [str]
        l = list(str)

        fi = open('input.txt', 'w')
        for i in range(len(inputs)):
            fi.write(inputs[i])
            if i != len(inputs) - 1:
                fi.write(' ')

        fi.close()

        wn = turtle.Screen()
        p = turtle.Turtle()

        for i in range(len(l)):
            dict[l[i]](p)

        wn.exitonclick()



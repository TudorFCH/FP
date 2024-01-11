def ersetzung(wordout,wordin):

    f = open("text.txt", "r")
    s=f.read()
    l=s.split()
    a=''
    ct=0
    for i in range(len(l)):
        if l[i]==wordout:
            l[i]=wordin
            ct+=1
        a=a+l[i]+' '

    f = open("text.txt", "w")
    f.write(a)
    f.close()
    if(ct>0):
        print('Das gewahlte Wort wurde ' + str(ct) + ' Mal ersetzt')
    else:
        print('Das gewahlte Wort befindet sich nicht in der Datei')

ersetzung('katze', 'katze')
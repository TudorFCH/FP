def ersetzung(wordout,wordin):

    f = open("C:\users\tudor\PycharmProjects\FP\Lab4\A2./text", "r")
    s=f.read()
    l=s.split(" ")
    a=''
    ct=0
    for i in range(len(l)):
        if l[i]==wordout:
            l[i]=wordin
            ct+=1
        a=a+l[i]+' '

    f = open("C:\users\tudor\PycharmProjects\FP\Lab4\A2./text", "w")
    f.write(a)
    f.close()
    if(ct>0):
        print('Das gewahlte Wort wurde ' + str(ct) + ' Mal ersetzt')
    else:
        print('Das gewahlte Wort befindet sich nicht in der Datei')
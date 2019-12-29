EAdict = [ {' ': ' ' } , {'a' : 'ا'} , {'b':'ب'} , {'c':'س'} , {'d':'د'} , {'e':'ي'} , {'f':'ف'} , {'g':'ج'} , 
         {'h':'ه'} , {'i':'ي'} , {'j':'ج'} , {'k':'ك'} , {'l':'ل'} , {'m':'م'} , {'n':'ن'} , {'o':'و'} , 
         {'p':'ب'} , {'q':None} , {'r':'ر'} , {'s':'س'} , {'t':'ت'} ,{'u':None} , {'v':'ف'} , {'w':'و'} ,
         {'y':'ي'} , {'z' : 'ز'} ] 
    

a = 'yasta'
b = [None] * len(a)
i = 0
    while i < len(a):
        if a[i] == ' ': # space
            b[i] = ' '
        if a[i] == 'w': # w
            b[i] = 'و'
        if a[i] == 'g': # g
            b[i] = 'ج'
        if a[i] == 'e': # e
            b[i] = 'ي'
        if a[i] == 'a': # a
            b[i] = 'ا'
        if a[i] == 's': # s
            b[i] = 'س'
        if a[i] == 'd': # d
            b[i] = 'د'
        if a[i] == 't': # t
            b[i] = 'ت'
        if a[i] == 'n': # n
            b[i] = 'ن'
        if a[i] == 'm': # m
            b[i] = 'م'
        if a[i] == 'l': # l
            b[i] = 'ل'
        if a[i] == 'k': # k
            b[i] = 'ك'
        if a[i] == '3': # m
            b[i] = 'ع'
        if a[i] == '2': # m
            b[i] = 'ق'
        if a[i] == '4': # m
            b[i] = 'ش'
        if a[i] == '7': # m
            b[i] = 'ح'
        if a[i] == 'h': # m
            b[i] = 'ه'
        if a[i] == 'f': # m
            b[i] = 'ف'
        if a[i] == 'o': # m
            b[i] = ''
        if a[i] == 'y': # m
            b[i] = 'ي'

                    
                    i +=1
elif text.startswith('/arabictofranko '):
                a = ' '.join(text.split(' ')[1:])
                b = [None] * len(a)
                i = 0
                while i < len(a):
                    if a[i] == ' ': # space
                        b[i] = ' '
                    if a[i] == 'و': # w
                        b[i] = 'w'
                    if a[i] == 'ج': # g
                        b[i] = 'g'
                    if a[i] == 'ي': # e
                        b[i] = 'e'
                    if a[i] == 'ا': # a
                        b[i] = 'a'
                    if a[i] == 'س': # s
                        b[i] = 's'
                    if a[i] == 'د': # d
                        b[i] = 'd'
                    if a[i] == 'ت': # t
                        b[i] = 't'
                    if a[i] == 'ن': # n
                        b[i] = 'n'
                    if a[i] == 'م': # m
                        b[i] = 'm'
                    if a[i] == 'ل': # l
                        b[i] = 'l'
                    if a[i] == 'ك': # k
                        b[i] = 'k'
                    if a[i] == 'ع': # 3
                        b[i] = '3'
                    if a[i] == 'ق': # 2
                        b[i] = '2'
                    if a[i] == 'ش': # 4
                        b[i] = '4'
                    if a[i] == 'ح': # 7
                        b[i] = '7'
                    if a[i] == 'ه': # h
                        b[i] = 'h'
                    if a[i] == 'ف': # f
                        b[i] = 'f'
                    if a[i] == 'o': # o
                        b[i] = ''
                    if a[i] == 'ي': # y
                        b[i] = 'y'
                    else:
                        b[i] = a[i]
                    
                    i +=1
                
                st = ''.join(b)
                send_message(st,chat) 
    
print(''.join(b))
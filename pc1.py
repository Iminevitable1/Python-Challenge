ques = input("Type your problem here: ")
ans = list(ques)
s = list()
for i in range(0,46):

    if (ord(ans[i]) + 2) == 123:
        temp = chr(97)
        s.append(temp)
    elif (ord(ans[i]) + 2) == 124:
        x = chr(98)
        s.append(x)
    elif (ord(ans[i]) + 2) == 34:
        y = chr(32)
        s.append(y)
    elif (ord(ans[i]) + 2) == 48:
        z = chr(46)
        s.append(z)
    elif (ord(ans[i]) + 2) == 42:
        a = chr(40)
        s.append(a)
    elif (ord(ans[i]) + 2) == 43:
        b = chr(41)
        s.append(b)
    elif (ord(ans[i]) + 2) == 41:
        c = chr(39)
        s.append(c)
    elif (ord(ans[i]) + 2) == 49:
        d = chr(47)
        s.append(d)
    elif (ord(ans[i]) + 2) == 60:
        e = chr(58)
        s.append(e)
    else:
        s.append(chr(ord(ans[i]) + 2))


q = ''.join(s)
print(q)


#    for j in range(0,1):
#        s = s[j] + s[j+1]
#
#    s = "".join(s)
#    print(s)

#for i in range(0,2):
#    ans = list(ans[i])
#ans = "".join(ans)
#print(ans)
#ch = chr(ord(ques) + 2)

#print(ch)

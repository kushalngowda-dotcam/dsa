def Atoi(s:str)->int:
    s=s.lstrip()
    if not s:
        return 0
    sign=1
    i=0
    if s[0]in['-','+']:
        if s[0]=='-':
            sign=-1
        i+=1
    num=0
    while i<len(s) and s[i].isdigit():
        num=num*10+(ord(s[i])-ord('0'))
        i+=1
    num*=sign
    intmin,intmax=-2**31,2**31-1
    if num<intmin:
        return  intmin
    if num>intmax:
        return intmax
    return num
print(Atoi('-42'))

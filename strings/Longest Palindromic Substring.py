def palindromes(s):
    if len(s)<2:
        return s
    start=0
    max_length=1
    def expandardcntr(left,right):
        nonlocal start,max_length
        while left>=0 and right<len(s) and s[left]==s[right]:
            if right-left+1 > max_length:
                start=left
                max_length=right-left+1
            left-=1
            right+=1
    for i in range(len(s)):
        expandardcntr(i,i)
        expandardcntr(i,i+1)
    return s[start:start+max_length]
s1=('abababba')
ob=palindromes(s1)
print(ob)

def lrs(s:str)->str:
    n=len(s)
    dp=[[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range (1,n+1):
            if s[i-1]==s[j-1] and i!=j:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    i,j=n,n
    lrs1=[]
    while i>0 and j>0:
        if s[i-1]==s[j-1] and i!=j:
            lrs1.append(s[i-1])
            i-=1
            j-=1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lrs1))
print(lrs("aaebbcdd"))
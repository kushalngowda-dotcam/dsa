def reversethewords(s):
    words=s.split()
    #words.reverse()
    words=words[::-1]
    return " ".join(words)
print(reversethewords("the sky is limit"))

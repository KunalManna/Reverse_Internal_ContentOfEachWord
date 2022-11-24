#Reverse internal content of each word in a string

def revInternalContent(s):
    p=s.split()
    l=[]
    for word in p:
        l.append(word[::-1])
        output=' '.join(l)
    return output


s=input("Enter the string:\n")               # Python is programming language
ans=revInternalContent(s)
print(ans)                                   # nohtyP si gnimmargorp egaugnal
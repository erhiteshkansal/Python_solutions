def CompeScore(p1,p2,s1,s2):
    a=max(p1,p2)
    b=max(s1,s2)
    if a==p1 and b==s1:
        score=10
    elif a==p2 and b==s2:
        score=10
    else:
        score=0
    return score 
a=CompeScore(20,17,21,16)
print a               
def ExtraScore(p1,p2,s1,s2):
    a=5-abs(p1-s1)
    b=5-abs(p2-s2)
    c=5-abs(abs(p1-p2)-abs(s1-s2))
    score=0
    if a<0 and b<0 and c<0:
        score=0
    elif b<0 and c<0:
        score=a
    elif a<0 and c<0:
        score=b
    elif a<0 and b<0:
        score=c    
    else:
        score=a+b+c
    return score
a=ExtraScore(21,17,17,13)
print a                
            
        
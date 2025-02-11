def predicScore(p11,p12,p21,p22):
    a=max(p11,p12)
    b=max(p21,p22)
    score=0
    if a==p11 and b==p21:
        score=0
    elif a==p12 and b==p22:
        score=0
    else:
        score=25
    return score            
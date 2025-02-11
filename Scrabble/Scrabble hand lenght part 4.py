def calculateHandlen(hand):
    c=0
    for d in hand.keys():
        c=c+hand[d]
    return c
z=calculateHandlen({'h':1,'e':1,'l':2,'o':0})
print z       
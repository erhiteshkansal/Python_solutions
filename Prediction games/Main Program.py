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
    
dick={}
para=raw_input('Parameters')
para1=int(para.split(' ')[0])
para2=int(para.split(' ')[1])
for q in range(para1):
    name=raw_input('Enter name')
    dick[name]=[]
    for w in range(para2):
        pred=raw_input('Enter predic')
        dick[name].append(int(pred.split(' ')[0]))
        dick[name].append(int(pred.split(' ')[1]))
dick['RealScore']=[] 
for w in range(para2): 
    realScore=raw_input('Enter real Score')
    dick['RealScore'].append(realScore.split(' ')[0])    
    dick['RealScore'].append(realScore.split(' ')[1])  
print dick    
imp=len(dick['RealScore'])
namelist=dick.keys()
print namelist
dick2={}
R1=0
R2=0
for r in namelist:
    for t in range(imp,2):
         R1=R1+CompeScore(dick[r][t],dick[r][t+1],dick['RealScore'][0],dick['RealScore'][1])
         print R1
         R2=R2+ ExtraScore(dick[r][t],dick[r][t+1],dick['RealScore'][0],dick['RealScore'][1])
         print R2
    TotalScore=R1+R2
    print TotalScore
    dick2[r]=TotalScore
Scorelist=dick2.values()         
a=max(dick2)
print dick2
for m in namelist:
    if dick2[m]==a:
        print m


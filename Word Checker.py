# Type your code here
def spelling_corrector(s1,s2):
    s=''
    checker=''
    s22=''
    flag1=0
    flag3=0
    s11=s1.lower()
    length=len(s11)
    for l in s11:
        if l!=' ' and flag1==0:
           s22=s22+l
        elif l!=' ' and flag1==1:
            flag1=0
            s22=s22+' '+l     
        elif l==' ':
            flag1=1
    print s22        
    nspace=s22.count(' ')          
    for i in range(0,nspace):
        checker=s22.split(' ')[i]
        if len(checker)==1 or len(checker)==2:
            s=s+checker+' '
        elif checker in s2:
           s=s+checker+' '
        elif checker=='the' or checker=='and':
            s=s+checker+' '   
        else:
           count=0
           flag=0
           for j in s2:
              j1=j.lower()
              if checker[0]==j1[0] or checker[0]==j1[1]:
                  if abs(len(checker)-len(j1))==1 or len(checker)==len(j1):
                      for k in checker:
                          if k in j1 and checker.count(k)==j1.count(k):
                              count=count+1
                      if count==len(checker) or count==len(j1) or abs(count-len(checker))==1 or abs(count-len(j1))==1:        
                        flag=1
                        s=s+j1+' '
                        break
           if flag!=1:           
             s=s+checker+' '
    checker=s22.split(' ')[-1]
    count=0
    flag=0
    for j in s2:
        j1=j.lower()
        if checker[0]==j1[0]:
            if abs(len(checker)-len(j1))==1 or len(checker)==len(j1):
                for k in checker:
                    if k in j1:
                        count=count+1      
                if count==len(checker) or count==len(j1)  or abs(count-len(checker))==1 or abs(count-len(j1))==1:        
                    flag=1
                    s=s+j1
                    break
    if flag!=1:
        s=s+checker
    return s       
 
a=spelling_corrector('Thes is the Firs cas',['that', 'first', 'case', 'car']) 
print a                          
                      
    
                      
                      
                  
           
           
        
        
def lcm(n,m):
   l1=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
   i=0
   cnt=0
   res=1
   flag=0
   for p in range(0,len(m)):
      m[p]=int(m[p])
   while(cnt!=n):
      for j in m:
         if j==1:
            cnt+=1
            
      if cnt!=n:
         cnt=0
      x=l1[i]
      
      for k in range(0,len(m)):
         if m[k]%x==0:
            flag=1
            m[k]=int(m[k]/x)
            
      if flag==0:
         i+=1
         
      if flag==1:
         res=res*x
         flag=0
         
   return res


a=int(input())
l1=[]
for i in range(0,a):
    b=input()
    l1.append(b.split(' ')) 
for i in range(0,a):
    if len(l1[i])>=2:
        if l1[i][0]=='A':
            try:
                l1[i][-1]=int(l1[i][-1])
            except:
                pass                               
dick={'Darrell':0,'Sally':0}       
for i in range(0,a):
    if (i+1)%2==1:
        if len(l1[i])==1:
            print ('Invalid Input')                
            break
        else:
            print (str(l1[i][0])+"'s question is : "+str(l1[i][1]))
            c=l1[i][-1].split(',')
            ans=lcm(len(c),c)  
    elif (i+1)%2==0:
        if len(l1[i])==3 and l1[i][0]=='A':
            if not (l1[i][1] in dick.keys()):
                dick[l1[i][1]]=0
            if l1[i][-1]=='PASS':
                print ('Question is PASSed')
                print ('Answer is: '+str(ans))
                print (str(l1[i][1])+': '+str(dick[l1[i][1]])+'points')
            elif type(l1[i][-1])==int:
                if ans==l1[i][-1]:
                    print ('Correct Answer')
                    dick[l1[i][1]]=dick[l1[i][1]]+10
                    print (str(l1[i][1])+': '+str(dick[l1[i][1]])+'points')
                else:
                    print ('Wrong Answer')
                    print (str(l1[i][1])+': '+str(dick[l1[i][1]])+'points')    
            else:
                print ('Invalid Input')
                break   
    if i==a-1:             
        print ('Total points:')
        print (str(l1[0][0])+': '+str(dick[l1[0][0]])+'points')
        print (str(l1[1][1])+': '+str(dick[l1[1][1]])+'points')
        ans=max(dick.values())
        count=0
        for i in dick.keys():
            if ans==dick[i]:
                count+=count+1
        if count>1:
            print ('Game Result: Draw')
        else:
            for i in dick.keys():
                if dick[i]==ans:
                    print ('Game Result: '+str(i)+' is winner')
                    break    

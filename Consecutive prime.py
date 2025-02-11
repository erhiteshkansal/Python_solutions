l1=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541]
number=int(input())
l2=[]
result=0
h1=1
if number<=1000:
    l2=l1[:]
elif number>1000:
    if int(number/5)<=l1[-1]:
        if (int(number/5)) in l1:
            ind=l1.index((int(number/5)))
            l2=l1[0:ind+1]
        else:
            l1.append((int(number/5)))
            l1.sort()
            ind=l1.index((int(number/5)))
            l2=l1[0:ind]
            l1.remove((int(number/5)))
    else:
        l2=l1[:]
        for i in range(l1[-1],int(number/5),2):
            for j in l1[1:int((number/5)**(1/2))]:
                if i%j==0:
                    h1=0
                    break
            if h1==1:
                l2.append(i)
                if (i in l1)==False:
                    l1.append(i)
            h1=1       
l3=[5]
for i in l2[2:]:
    if l3[-1]+i>number:
        break
    l3.append(l3[-1]+i)
for i in l3:
    if i%3!=0:
        if i in l1:
            result=result+1
        else:
            for j in l1:
                if i%j==0:
                    h1=0
                    break
            if h1==1:
                result=result+1
            h1=1            
print(result)    

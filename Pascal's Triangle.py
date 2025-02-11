def MY_2D_LIST(n):
    if n==1:
        return [[1]]
    elif n==2:
        return [[1],[1,1]]
    else:
        list1=[[1],[1,1]]
        index=1
        list2=[]
        while n>2:
            list2.append(list1[index][0])
            for i in range(0,len(list1[index])):
                if i==len(list1[index])-1:
                    list2.append(list1[index][i]) 
                else:
                    list2.append(list1[index][i]+list1[index][i+1])
            list1.append(list2)
            list2=[]
            index=index+1
            n=n-1                  
    return list1
            
a=MY_2D_LIST(8) 
print a               
def a(secretword,guess):
    s=secretword
    c=0
    for f in secretword:
        if f in guess:
            c=c+1
            print (c)
        else:    
            s=s.replace(f,'_')
    return s        
def b(secretword,guess):
    a=len(secretword)
    c=0
    for e in guess:
        if e in secretword:
            c=c+1
    if c==a:
        return True
    else:
        return False       
import string
# print (string.ascii_lowercase)
def c(letterguess):
    a=string.ascii_lowercase
    b=string.ascii_lowercase
    for e in letterguess:
        if e in a:
           b=b.replace(e,'')
           print (b)             
def d(hangman):
    w=''
    q=1
    while(q<=8):
       q=q+1 
       z=input('Enter guess ')
       if z in w:
           print ('Same choice guess again')
       elif b(hangman,z)==True:
             test2=a(hangman,z)
             print (test2)
             c(z)
       else:
             print ('Sorry wrong guess')
       w=w+z           
d('apple')        
    
    
    
    
               
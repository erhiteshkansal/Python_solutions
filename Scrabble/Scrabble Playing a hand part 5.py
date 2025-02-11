def playHand(hand, wordList, n):
    f=0
    s=0
    z=''
    while z!='.':
        o=''
        for t in hand.keys():
           for y in range(hand[t]):
              o=o+str(t)+' '
        print 'Current Hand: '+ o
        z=raw_input('Enter word, or a "." to indicate that you are finished: ')
        if z=='.':
            print 'Goodbye! Total score: '+str(s)+' points.'
            break
        elif isValidWord(z,hand,wordList)==True:
             f=getWordScore(z, n)
             s=s+f
             print '"'+str(z)+'"'+' earned '+str(f)+' points. Total: '+str(s)+' points'
             print ''
             hand=updateHand(hand,z)
             e=hand.values()
             if e.count(0)==len(hand):
                 print 'Run out of letters. Total score: '+str(s)+' points.'
                 break
        else:
             print 'Invalid word, please try again.'     
           
                         
def isValidWord(word, hand, wordList):
    c=0
    if word in wordList:
        for letters in word:
            if hand.get(letters,0)==0:
                return False
            elif hand[letters]>=word.count(letters):        
                 c=c+1
            else:
                return False    
        return True
    else:
        return False            
            
            
def updateHand(hand, word):
   for letters in word:
       hand[letters]=hand[letters]-1
   return hand             
   
def getWordScore(word, n):
   SCRABBLE_LETTER_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
} 
   sum=0
   for letter in word:
      sum=sum+SCRABBLE_LETTER_VALUES[letter] 
   if n==len(word):
       return (sum*n)+50
   else:
       return sum*len(word)   
       
playHand({'d':1,'e':1,'l':2,'o':1,'g':1,'c':1,'a':1,'t':1,'h':1},('hello','hell','dog','cat'),10)        
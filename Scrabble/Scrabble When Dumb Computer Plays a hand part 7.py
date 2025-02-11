def compChooseWord(hand, wordList, n):
       z=0
       s=''
       for word in wordList:
                if isValidWord(word, hand, wordList)==True:
                    t=getWordScore(word, n)
                    if t>z:
                       s=word
                       z=t
       if s=='':
          return None
       else:   
          return s
   
   
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
   

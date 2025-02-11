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

z=isValidWord('hello',{'h': 0, 'e': 9, 'l': 2, 'o': 1},('hello','hellllll','heg'))
print z
   
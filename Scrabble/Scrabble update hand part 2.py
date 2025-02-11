def updateHand(hand, word):
   a={}
   for letters in hand.keys():
       if letters in word:
           if hand[letters]!=0:
              a[letters]=hand[letters]-word.count(letters)
           else:
              a[letters]=0  
       else:
           a[letters]=hand[letters]         
   return a
z=updateHand({'q': 3, 'i': 1, 'r': 3, 'e': 3, 't': 3, 'w': 3, 'p': 3, 'y': 3, 'u': 3, 'o': 3}, 'typewriter')
print z
      
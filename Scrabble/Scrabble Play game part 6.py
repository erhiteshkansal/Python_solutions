def playGame(wordList):
    c=1
    z=''
    while z!='e':
       z=raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
       if c==1 and z=='r':
          print 'You have not played a hand yet. Please play a new hand first!'
       elif z=='n':
          c=c+1
          hl=dealHand(HAND_SIZE)    ### given by edx
          n=HAND_SIZE
          playHand(hl, wordList,n)
       elif z=='r':
          playHand(hl, wordList,n)
       elif z=='e':
          break
       else:
          print 'Invalid command.'
          
          
       
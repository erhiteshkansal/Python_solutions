# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 23:20:29 2017

@author: Virus
"""
import numpy as np
attack=[]
board=[0,0,0,0,0,0,0,0]
for it in range(0,8):
    attack.append(board[:])
def placequeen(i,board,attack):
    if 0 in attack[i-1]:
        for c in range(0,8):
            if attack[i-1][c]==0:
                attack[i-1][c]=i
                board[c]=i
                if i == len(board):
                    return True
                else:
                    #print(np.array(attack))
                    attack=update_attack(attack,i,c)
                    #print(np.array(attack))
                    #break
                    extendsoln=placequeen(i+1,board,attack)
                    print(np.array(attack))
                    print(np.array(board))
                if extendsoln:
                    return True
                else:
                    attack[i-1][c]=0
                    attack=undo_attack(attack,i,c)
                    #print(np.array(attack))
                    board[c]=0
    else :
        return False
    print(np.array(attack))
    print(np.array(board))
def update_attack(attack,i,c):
    for j in range(0,8):
        if attack[i-1][j]<1:
            attack[i-1][j]+=-1
    #print(np.array(attack[i-1]))
    for j in range(i-1,8):
        if attack[j][c]<1:
            attack[j][c]+=-1
   
    inc=1
    while (c-inc)>-1 and (i-1+inc)<8:
        attack[i-1+inc][c-inc]+=-1
        inc+=1
        
    dnc=1
    while (c+dnc)<8 and (i-1+dnc)<8:
        attack[i-1+dnc][c+dnc]+=-1
        dnc+=1
    return attack

def undo_attack(attack,i,c):
    for j in range(0,8):
        if attack[i-1][j]<0:
            attack[i-1][j]+=1
    for j in range(i-1,8):
        if attack[j][c]<0:
            attack[j][c]+=1
        
    inc=1
    while (c-inc)>-1 and (i-1+inc)<8:
        attack[i-1+inc][c-inc]+=1
        inc+=1
        
    dnc=1
    while (c+dnc)<8 and (i-1+dnc)<8:
        attack[i-1+dnc][c+dnc]+=1
        dnc+=1
    return attack

placequeen(1,board,attack)
            

        
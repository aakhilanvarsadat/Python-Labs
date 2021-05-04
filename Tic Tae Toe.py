#!/usr/bin/env python
# coding: utf-8

# In[ ]:


b=[" "," "," "," "," "," "," "," "," "]
positions=[1,2,3,4,5,6,7,8,9]
posub=[]
tie=False


# In[ ]:


from IPython.display import clear_output


# In[ ]:


def win():
    global winning,tie
    if(b[0]==b[1]==b[2]=='X' or b[3]==b[4]==b[5]=='X' or b[6]==b[7]==b[8]=='X' or b[0]==b[4]==b[8]=='X' or b[2]==b[4]==b[6]=='X' or b[0]==b[3]==b[6]=="X" or b[1]==b[4]==b[7]=="X" or b[2]==b[5]==b[8]=="X" or b[0]==b[1]==b[2]=='O' or b[3]==b[4]==b[5]=='O' or b[6]==b[7]==b[8]=='O' or b[0]==b[4]==b[8]=='O' or b[2]==b[4]==b[6]=='O' or b[0]==b[3]==b[6]=="O" or b[1]==b[4]==b[7]=="O" or b[2]==b[5]==b[8]=="O"):
        winning=True
        print("Match won")
    else:
        winning=False
    if(b[0]!=" " and b[1]!=" " and b[2]!=" " and b[3]!=" " and b[4]!=" " and b[5]!=" " and b[6]!=" " and b[7]!=" " and b[8]!=" "):
        print("Match Tie")
        tie=True


# In[ ]:


def display_board():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    print("   |   |   ")
    print(f" {b[0]} | {b[1]} | {b[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {b[3]} | {b[4]} | {b[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {b[6]} | {b[7]} | {b[8]} ")
    print("   |   |   ")


# In[ ]:


sym=['X','O']


# In[ ]:


print("Welcome to Aakhil's Tic Tac Toe vibes")
case1=False
case2=False
winning=False
p1=[]
p2=[]
casenum=1
while(case1==False):
    symbol=input("Player 1: Do you want to be X or O:- ")
    if symbol not in sym:
        case1=False
        print("Sorry,Invalid symbol!!!")
    else:
        case1=True
if symbol=="X":
    print("Player 1 is X and Player 2 is O")
    print("Player 1 plays first!!!")
else:
    print("Player 2 is X and Player 1 is O")
    print("Player 2 plays first!!!")
display_board()
while(winning==False):
    while(case2==False):
        pos=int(input("Choose the position 1-9"))
        if (pos in positions) and (pos not in posub):
            case2=True
            if casenum%2==0:
                b[pos-1]='O'
            else:
                b[pos-1]='X'
        else:
            print("Sorry, please type an available integer from 1 to 9")
            case2=False
        posub.append(pos)
    casenum=casenum+1
    case2=False
    clear_output()
    display_board()
    win()
    if winning ==True:
        print("Congratulations!!! You won the game")
    if tie==True:
        winning=True


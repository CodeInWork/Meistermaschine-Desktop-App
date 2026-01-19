
from random import randint


def roll_destiny()->tuple[int, str]:

    diceRoll = randint(1, 20)
    if diceRoll == 1:
        outPutStr = "\u2620"
        
    elif 1 < diceRoll <= 5:
        outPutStr = "\u2620\u2620"
    elif 5 < diceRoll <= 9:
        outPutStr = "\u2620"
    elif 9 < diceRoll <= 11:
        outPutStr = "\u2665 \u2620"
    elif 11 < diceRoll <=15:
        outPutStr = "\u2665" 
    elif 15 < diceRoll <= 19:
        outPutStr = "\u2665\u2665"
    else:   # natural 20
        outPutStr =  "\u2665"
        

    return diceRoll, outPutStr


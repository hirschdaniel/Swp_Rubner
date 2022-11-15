import random

import numpy as np


def Poker():
    c = []

    for i in range(0, 52):
        c.append(i)

    cards = np.array(c)

    f = 51
    for j in range(0, 52):
        a = random.randrange(0, 52, 1)
        y = cards[a]
        z = cards[f]
        cards[f] =y
        cards[a] = z
        f = f - 1
    global color
    color = np.floor_divide(cards[1:7], 13)

    global card_symbol
    card_symbol = cards[1:7] % 13

    paar()
    drilling()
    vierling()
    Strasse()
    fullHouse()
    flush()
    straightFlush()
    royalFlush()






def paar():
    zaehler = 0

    for i in range(1,6):
        for j in range(1,6):
            if card_symbol[j] == card_symbol[i]:
                zaehler += 1

        if zaehler == 2:
            return True
        else:
            return False


def drilling():
    zaehler = 0

    for i in range(1,6):
        for j in range(1, 6):
            if card_symbol[j] == card_symbol[i]:
                zaehler = zaehler+1

        if zaehler == 3:
            return True
        else:
            return

def vierling():
    zaehler = 0

    for i in range(1,6):
        for j in range(1, 6):
            if card_symbol[j] == card_symbol[i]:
                zaehler = zaehler+1

        if zaehler == 4:
            return True
        else:
            return False


def Strasse():
    zaehler = 0
    card_symbol_strasse = np.sort(card_symbol)[::-1]
    strasse = card_symbol_strasse[1]
    for i in range(2,6):
        if card_symbol_strasse[i]<strasse:
            strasse = strasse -1
            zaehler = zaehler+1
    if zaehler == 4:
        return True
    else:
        return False


def fullHouse():
    if(drilling() == True and paar() == True ):
        drilling()==False
        paar() == False
        return True
    else:
        return False


def flush():
    if(color[1]== color[2] == color[3] == color[4] == color[5]):
        return True
    else: return False


def straightFlush():
    # A-K-Q-J-10
    # 13 karten: A= 1, k=13, Q=12, J=11, 10=10
    card_symbol_straightFlush = np.sort(card_symbol)[::-1]
    if(card_symbol_straightFlush[1]==13 and card_symbol_straightFlush[2]==12 and card_symbol_straightFlush[3]==11 and card_symbol_straightFlush[4]==10 and card_symbol_straightFlush[5]==1):
        return True
    else: return False



def royalFlush():
    if(straightFlush()==True and flush()== True):
        straightFlush()== False;
        flush()== False;
        return True
    else: return False






























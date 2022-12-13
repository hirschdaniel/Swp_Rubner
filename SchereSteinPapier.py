from random import random, randrange

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    with open("data.txt", "r") as f:
        txt = f.read()
    return txt




symbol = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]

def mode_choice():
    mode = input("Bitte geben sie a für advanced ,n für normal ein, d fürs einsehen der daten ein oder s fürs starten des servers")
    if mode != 'n' or mode !='a' or mode != 'd' or mode != 's':
        print("Du hast ", mode,"eingegeben")
        return mode
    else:
        print('Du musst n, a oder d eingeben  ')


def userInput():
    while True:
        try:
            userinput = int(input("Bitte geben sie 1 (Stein), 2 (Papier), 3(Schere) 4(Spock)  oder 5 (Echse) ein: "))
        except ValueError:
            print("Es muss eine zahl sein")
            continue
        if userinput >= 1 and userinput <= 5:
            print("Du hast ", userinput, "(",symbol[userinput], ") eingegeben")
            return userinput
            break
        else:
            print('Die Zahl muss zwischen 1 und 5 sein ')





def getwinner(n1, n2):
    if(n1 == n2):
        return 2
        print("unentschieden")
    if(n1 == (n2+1)%4 or (n2+3)%4 ):
        return 1
    return 0

def comp():
    compchoice = randrange(1,6)
    return compchoice



def saveData(winner, s_compchoice, s_userinput):
    with open("data.txt", "a") as f:
        stri = str(winner) +','+  str(s_compchoice) +','+ str(s_userinput) +","
        f.write(stri)


def getData():
    with open("data.txt", "r") as f:
        txt = f.read()
    return txt


def analyse(txt):
    l1 = []
    data = []
    l1 = txt.split(',')
    for i in range(2, len(l1), 3):
        data.append(l1[i])
    counter = 0
    num = data[0]
    for i in data:
        curr_frequency = data.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    c = (int(num)+1)%4
    return c





def main():
    m =  mode_choice()
    if (m == 's'):
        app.run()

    if (m == 'd'):
        print(getData())


    if(m=='a'):
        co = analyse(getData())
    else:
        co = comp()

    ui = userInput()

    print("Computer wählt:", co, "(", symbol[co - 1], ")")

    if (getwinner(ui, co) == 1):
            print("Du hast gewonnen!")
            w = 1
    elif(getwinner(ui, co) == 0):
            print("Computer hat gewonnen!")
            w = 2
    elif(getwinner(ui, co) == 2):
            print("Unentschieden")
            w=3

    saveData(w, co, ui)
    print(analyse(getData()))


if __name__ == "__main__":
    main()





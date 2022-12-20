import json
from random import randrange

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    with open("data.txt", "r") as f:
        txt1 = f.read()
    data = []
    txt = txt1.split(",")
    for i in range(0,len(txt),3):
        str = "Winner", txt[i], "ComputerChoice", txt[i + 1], "UserChoice", txt[i + 2]
        data.append(str)
        jsonData = json.dumps(data)
    return jsonData

symbol = ["Rock", "Lizard", "Spock", "Scissors", "Paper"]

def mode_choice():
    mode = input("Bitte geben sie a für advanced ,n für normal, d fürs einsehen der statistiken oder s fürs starten des servers ein")
    if mode != 'n' or mode != 'a' or mode != 'd' or mode != 's':
        print("Du hast ", mode,"eingegeben")
        return mode
    else:
        print('Du musst n, a oder d eingeben')


def userInput():
    while True:
        try:
            userinput = int(input("Bitte geben sie 0 (Stein), 1 (Echse), 2(Spock) 3(Schere)  oder 4 (Papier) ein: "))
        except ValueError:
            print("Es muss eine zahl sein")
            continue
        if userinput >= 0 and userinput <= 4:
            print("Du hast ", userinput, "(",symbol[userinput], ") eingegeben")
            return userinput
            break
        else:
            print('Die Zahl muss zwischen 0 und 4 sein ')

##useri, comp
symbol = ["Rock", "Lizard", "Spock", "Scissors", "Paper"]
def getwinner(p1, comp):
    if(p1 == comp):
        return 0
        print("unentschieden")
    elif((p1+1)%5 == comp or (p1+3)%5 == comp ):
        return 1 #userwins
    else:
        return 2 #comwins



def comp():
    compchoice = randrange(0,4)
    return compchoice


def saveData(winner, s_compchoice, s_userinput):
    with open("data.txt", "a") as f:
        stri = str(winner) +','+  str(s_compchoice) +','+ str(s_userinput) +","
        f.write(stri)


def getData():
    with open("data.txt", "r") as f:
        txt = f.read()
    return txt

def dataToStatistics():

    l = getData().split(",")
    userwin = 0
    compwin = 0
    draw = 0

    for i in range (0, len(l), 3):
        if(l[i] == '1'):
            userwin = userwin + 1
        if(l[i]== '2'):
            compwin = compwin + 1
        if(l[i]=='3'):
            draw = draw +1
    games = draw + compwin + userwin
    print(" Es gab: ", games, "Spiele. Der Computer hat", compwin, " mal (", compwin/games*100,"%) gewonnen, der Spieler hat: ", userwin, " mal (", userwin/games*100,"%) gewonnen, und es war: ",draw," (",draw/games*100," unentschieden")



def analyse(txt):
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
        dataToStatistics()

    if(m=='a'):
        co = analyse(getData())
    else:
        co = comp()

    ui = userInput()

    print("Computer wählt:", co, "(", symbol[co - 1], ")")

    if (getwinner(ui, co) == 1):
            print("Du hast gewonnen!")
            w = 1
    elif(getwinner(ui, co) == 2):
            print("Computer hat gewonnen!")
            w = 2
    elif(getwinner(ui, co) == 0 ):
            print("Unentschieden")
            w=0

    saveData(w, co, ui)
    print(analyse(getData()))


if __name__ == "__main__":
    main()

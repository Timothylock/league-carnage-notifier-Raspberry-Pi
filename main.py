from modules import teamInfo
from modules.datasave import datasave
from modules import dispData
from modules import test
from modules.speech import tts
from modules.disp import disp
from modules.pinsIO import gpio
import time

#User Variables
username = "timthedude"

while True:
    disp.display("Player not in a game", "  join a 5v5 match  ", "", "")
    gpio.on(6)
    teamInfo.getTeam(username)

    start = datasave.read("data/teaminfo.dat")

    try:
        while start[0] == "nogame":
            print("Player not in game / Game not observable")
            time.sleep(5) #time delay in seconds
            teamInfo.getTeam(username)
            start = datasave.read("data/teaminfo.dat")
    except:
        print ("Game Started")
    gpio.off(6)
    tts.speak("The game is now starting. Calculating game data")
    dispData.show(start)
    disp.clear()
    disp.display(" Predicting Winners ", "   please wait...   ", "", "")
    result = test.winOrLose(start)
    disp.display(result[0][0:20],result[0][20:40], result[0][40:60], result[0][60:])
    tts.speak(result[0])
    disp.display(result[1][0:20],result[1][20:40], result[1][40:60], result[1][60:])
    tts.speak(result[1])
    while True:
        dispData.show(start)
        disp.display(result[0][0:20],result[0][20:40], result[0][40:60], result[0][60:])
        time.sleep(6)
        disp.display(result[1][0:20],result[1][20:40], result[1][40:60], result[1][60:])
        time.sleep(6)
        try:
            if (start[0] == "nogame"):
                break
        except:
            print ("Game has not ended")
    

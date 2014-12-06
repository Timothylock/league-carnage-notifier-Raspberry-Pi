from modules import teamInfo
from modules.datasave import datasave
import time

#User Variables
username = "arexxkd"

teamInfo.getTeam(username)

start = datasave.read("data/teaminfo.dat")

try:
    while start[0] == "nogame":
        print("Player not in game / Game not observable")
        time.sleep(5) #time delay in seconds
        teamInfo.getTeam(username)
        start = datasave.read("data/teaminfo.dat")
except:
    print
print("Game has started")


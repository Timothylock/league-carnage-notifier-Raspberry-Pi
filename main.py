from modules import gameload
from modules.datasave import datasave
import time

#User Variables
username = Commit

gameload.getTeam(username)

start = datasave.read("modules/data/teaminfo.dat")
while start[0] == "nogame":
    time.sleep(5) #time delay in seconds
    gameload.getTeam(username)
    start = datasave.read("modules/data/teaminfo.dat")

print("Game has started")

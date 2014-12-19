from speech import tts
import time
import os
from disp import disp

def show (stat):
    t1name = []
    t2name = []

    # Put the names into lists
    for i in range(5):
        t1name.append(stat["team1"]["player" + str(i+1)][5])
    for i in range(5):
        t2name.append(stat["team2"]["player" + str(i+1)][5])

    print(len(t2name[1]))
        
    # Add spaces to deal with short names
    for i in range(5):
        t1name[i] = t1name[i] + "       "
    for i in range(5):
        t2name[i] = t2name[i] + "       "

    # Shorten the lists
    for i in range(5):
        if len(t1name[i]) >= 7:
            t1name[i] = (t1name[i])[0:6]
    for i in range(5):
        if len(t2name[i]) >= 7:
            t2name[i] = (t2name[i])[0:6]

    os.system('cls' if os.name == 'nt' else 'clear')

    for i in range(2):
        # Display
        line1 = "  Summoner Levels   "
        line2 = "                     "
        line3 = "                     "
        line4 = "                     "
        print (line1)
        print (line2)
        print (line3)
        print (line4)
	disp.display(line1,line2,line3,line4)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

	line4 = "  Team 1    Team 2  "
	print (line1)
        print (line2)
        print (line3)
        print (line4)
	disp.display(line1,line2,line3,line4)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

	line3 = "  Team 1    Team 2  "
        line4 = t1name[0] + " " + str(stat["team1"]["player3"][4]) + " " + t2name[0] + " " + str(stat["team2"]["player3"][4])
        print (line1)
        print (line2)
        print (line3)
        print (line4)
	disp.display(line1,line2,line3,line4)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

	line2 = "  Team 1    Team 2  "
        line3 = t1name[0] + " " + str(stat["team1"]["player2"][4]) + " " + t2name[0] + " " + str(stat["team2"]["player2"][4])
        line4 = t1name[1] + " " + str(stat["team1"]["player3"][4]) + " " + t2name[1] + " " + str(stat["team2"]["player3"][4])
        print (line1)
        print (line2)
        print (line3)
        print (line4)
	disp.display(line1,line2,line3,line4)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        line2 = t1name[0] + " " + str(stat["team1"]["player1"][4]) + " " + t2name[0] + " " + str(stat["team2"]["player1"][4])
        line3 = t1name[1] + " " + str(stat["team1"]["player2"][4]) + " " + t2name[1] + " " + str(stat["team2"]["player2"][4])
        line4 = t1name[2] + " " + str(stat["team1"]["player3"][4]) + " " + t2name[2] + " " + str(stat["team2"]["player3"][4])
        print (line1)
        print (line2)
        print (line3)
        print (line4)
	disp.display(line1,line2,line3,line4)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        line2 = t1name[1] + " " + str(stat["team1"]["player1"][4]) + " " + t2name[1] + " " + str(stat["team2"]["player1"][4])
        line3 = t1name[2] + " " + str(stat["team1"]["player2"][4]) + " " + t2name[2] + " " + str(stat["team2"]["player2"][4])
        line4 = t1name[3] + " " + str(stat["team1"]["player3"][4]) + " " + t2name[3] + " " + str(stat["team2"]["player3"][4])
        print (line1)
        print (line2)
        print (line3)
        print (line4)
	disp.display(line1,line2,line3,line4)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        line2 = t1name[2] + " " + str(stat["team1"]["player1"][4]) + " " + t2name[2] + " " + str(stat["team2"]["player1"][4])
        line3 = t1name[3] + " " + str(stat["team1"]["player2"][4]) + " " + t2name[3] + " " + str(stat["team2"]["player2"][4])
        line4 = t1name[4] + " " + str(stat["team1"]["player3"][4]) + " " + t2name[4] + " " + str(stat["team2"]["player3"][4])
        print (line1)
        print (line2)
        print (line3)
        print (line4)
	disp.display(line1,line2,line3,line4)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        line2 = t1name[3] + " " + str(stat["team1"]["player1"][4]) + " " + t2name[3] + " " + str(stat["team2"]["player1"][4])
        line3 = t1name[4] + " " + str(stat["team1"]["player2"][4]) + " " + t2name[4] + " " + str(stat["team2"]["player2"][4])
        line4 = "                     "
        print (line1)
        print (line2)
        print (line3)
        print (line4)
	disp.display(line1,line2,line3,line4)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        line2 = t1name[4] + " " + str(stat["team1"]["player1"][4]) + " " + t2name[4] + " " + str(stat["team2"]["player1"][4])
        line3 = "                     "
        line4 = "                     "
        print (line1)
        print (line2)
        print (line3)
        print (line4)
	disp.display(line1,line2,line3,line4)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        line2 = "                     "
        line3 = "                     "
        line4 = "                     "
        print (line1)
        print (line2)
        print (line3)
        print (line4)
	disp.display(line1,line2,line3,line4)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')


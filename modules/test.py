import unirest
from datasave import datasave

def getInfo(summonerID):
  response = unirest.get("https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/" + str(summonerID) + "/recent?api_key=4ef4ddb0-44e4-4757-8cd5-6aa9f512a813",
    headers={
    }
  )
  return(response.body)
  
def winOrLose(stats):
  wlRatio1 = []
  kdRatio1 = []
  gamesWon1 = 0
  gamesLoss1 = 0
  numKills1 = 0
  numDeaths1 = 0
  avgwl1 = 0
  avgkd1 = 0
  wl1 = 0
  kd1 = 0
  
  wlRatio2 = []
  kdRatio2 = []
  gamesWon2 = 0
  gamesLoss2 = 0
  numKills2 = 0
  numDeaths2 = 0
  avgwl2 = 0
  avgkd2 = 0
  wl2 = 0
  kd2 = 0

  players = stats
  name1 = []
  sId1 = []
  cId1 = []
  chmpName1 = []

  name2 = []
  sId2 = []
  cId2 = []
  chmpName2 = []

  for player in range(len(players["team1"])):
    name1.append(players["team1"]["player"+ str(player+1)][0])
    sId1.append(players["team1"]["player"+ str(player+1)][1])
    cId1.append(players["team1"]["player"+ str(player+1)][3])
    chmpName1.append(players["team1"]["player"+ str(player+1)][5])
    
  for player in range(len(players["team2"])):
    name2.append(players["team2"]["player"+ str(player+1)][0])
    sId2.append(players["team2"]["player"+ str(player+1)][1])
    cId2.append(players["team2"]["player"+ str(player+1)][3])
    chmpName2.append(players["team2"]["player"+ str(player+1)][5])

  for summoner in range(len(sId1)):
    response = getInfo(sId1[summoner])
    for games in range(len(response["games"])):
      if cId1[summoner] == response["games"][games]["championId"]:
        #numKills1 += response["games"][games]["stats"]["championsKilled"]
        #numDeaths1 += response["games"][games]["stats"]["numDeaths"]
        if response["games"][games]["stats"]["win"] == True:
          gamesWon1 += 1
        if response["games"][games]["stats"]["win"] == False:
          gamesLoss1 += 1
    if gamesLoss1 > 0:
      wlRatio1.append(gamesWon1/gamesLoss1)
    else:
      wlRatio1.append(gamesWon1)

    if numDeaths1 > 0:
      kdRatio1.append(numKills1/numDeaths1)
    else:
      kdRatio1.append(numKills1)
      
  for summoner in range(len(sId2)):
    response = getInfo(sId2[summoner])
    for games in range(len(response["games"])):
      if cId2[summoner] == response["games"][games]["championId"]:
        #numKills2 += response["games"][games]["stats"]["championsKilled"]
        #numDeaths2 += response["games"][games]["stats"]["numDeaths"]
        if response["games"][games]["stats"]["win"] == True:
          gamesWon2 += 1
        if response["games"][games]["stats"]["win"] == False:
          gamesLoss2 += 1
    if gamesLoss2 > 0:
      wlRatio2.append(gamesWon2/gamesLoss2)
    else:
      wlRatio2.append(gamesWon2)

    if numDeaths2 > 0:
      kdRatio2.append(numKills2/numDeaths2)
    else:
      kdRatio2.append(numKills2)


  for ratio in wlRatio1:
    wl1 += ratio
  avgwl1 = wl1/(len(wlRatio1))

  for ratio in kdRatio1:
    kd1 += ratio
  avgkd1 = kd1/(len(kdRatio1))                   

  for ratio in wlRatio2:
    wl2 += ratio
  avgwl2 = wl2/(len(wlRatio2))

  for ratio in kdRatio2:
    kd2 += ratio
  avgkd2 = kd2/(len(kdRatio2))
                       
  if avgwl1 < avgwl2 and avgkd1 < avgkd2:
    print("team 2 will most likely win")
  
  if avgwl1 < avgwl2 and avgkd1 > avgkd2:
    print("team 2 has a chance of winning")

  if avgwl1 > avgwl2 and avgkd1 < avgkd2:
    print("team 1 has a chance of winning")
  
  if avgwl1 > avgwl2 and avgkd1 > avgkd2:
    print("team 1 will most likely win")

  highestkd1 = kdRatio1.index(max(kdRatio1))
  highestkd2 = kdRatio2.index(max(kdRatio2))

  print("player: " +name1[highestkd1]+ " playing " + chmpName1[highestkd1] + " on team 1 is the highest threat")
  print("player: " +name2[highestkd2]+ " playing " + chmpName2[highestkd2] + " on team 2 is the highest threat") 
  return(("player: " +name1[highestkd1]+ " playing " + chmpName1[highestkd1] + " on team 1 is the highest threat"),("player: " +name2[highestkd2]+ " playing " + chmpName2[highestkd2] + " on team 2 is the highest threat"))

               
                       

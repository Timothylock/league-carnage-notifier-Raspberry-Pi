import unirest

def getTeam(summonerID):
  response = unirest.get("https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/" + str(summonerID) + "/recent?api_key=4ef4ddb0-44e4-4757-8cd5-6aa9f512a813",
    headers={
    }
  )
  return(response.body)

def winOrLose(championsID, response):
  wlRatio = 0
  kdRatio = 0
  gamesWon = 0
  gamesLoss = 0
  numKills = 0
  numDeaths = 0
  for games in range(10):
    if championsID == response["games"][games]["championId"]:
      numKills += response["games"][games]["stats"]["championsKilled"]
      numDeaths += (response["games"][games]["stats"]["numDeaths"])
      if response["games"][games]["stats"]["win"] == "true":
        gamesWon += 1
      if response["games"][games]["stats"]["win"] == "false":
        gamesLoss += 1
        
  if gamesLoss > 0:
    wlRatio = gamesWon/gamesLoss
  else:
    wlRatio = gamesWon
  
  if numDeaths > 0:
    kdRatio = numKills/numDeaths
  else:
    kdRatio = numKills

  if gamesWon > 0:
    print("W/L Ratio: " + wlRatio)
  else:
    print("Unable to calculate W/L Ratio")
    
  if numKills > 0:
    print("K/D Ratio: " +kdRatio)
  else:
    print("Unable to calculate K/D Ratio")

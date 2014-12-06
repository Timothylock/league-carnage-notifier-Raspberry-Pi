import unirest

def getTeam(summonerID):
  response = unirest.get("https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/" + str(summonerID) + "/recent?api_key=4ef4ddb0-44e4-4757-8cd5-6aa9f512a813",
    headers={
    }
  )
  return(response.body)

def getFellowPlayers(response):
  for games in range(10):
    for players in range(8):
      print(response["games"][games]["fellowPlayers"][players]["summonerId"])
  

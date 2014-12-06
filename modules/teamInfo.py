import unirest
from datasave import datasave

def getTeam(player):
  # Init Variables
  stat = {}
  stat["team1"] = {}
  stat["team2"] = {}
  stat["team1"]["player1"] = []
  stat["team1"]["player2"] = []
  stat["team1"]["player3"] = []
  stat["team1"]["player4"] = []
  stat["team1"]["player5"] = []
  stat["team2"]["player1"] = []
  stat["team2"]["player2"] = []
  stat["team2"]["player3"] = []
  stat["team2"]["player4"] = []
  stat["team2"]["player5"] = []

  # Pull Team Data
  response = unirest.get("https://spectator-league-of-legends-v1.p.mashape.com/lol/na/v1/spectator/by-name/" + player,
    headers={
      "X-Mashape-Key": "cr1TQBbsvzmshKj7odQmhnN9xkFep149Dttjsnqs3Af4zb6rQH"
    }
  )
  data = response.body
  if ("error" not in data["data"]):  # Make sure that there is actually a game going on
    # Summoner Name
    stat["team1"]["player1"].append(data["data"]["game"]["teamOne"][0]["summonerName"])
    stat["team1"]["player2"].append(data["data"]["game"]["teamOne"][1]["summonerName"])
    stat["team1"]["player3"].append(data["data"]["game"]["teamOne"][2]["summonerName"])
    stat["team1"]["player4"].append(data["data"]["game"]["teamOne"][3]["summonerName"])
    stat["team1"]["player5"].append(data["data"]["game"]["teamOne"][4]["summonerName"])
    stat["team2"]["player1"].append(data["data"]["game"]["teamTwo"][0]["summonerName"])
    stat["team2"]["player2"].append(data["data"]["game"]["teamTwo"][1]["summonerName"])
    stat["team2"]["player3"].append(data["data"]["game"]["teamTwo"][2]["summonerName"])
    stat["team2"]["player4"].append(data["data"]["game"]["teamTwo"][3]["summonerName"])
    stat["team2"]["player5"].append(data["data"]["game"]["teamTwo"][4]["summonerName"])

    # Summoner Acc ID
    stat["team1"]["player1"].append(data["data"]["game"]["teamOne"][0]["summonerId"])
    stat["team1"]["player2"].append(data["data"]["game"]["teamOne"][1]["summonerId"])
    stat["team1"]["player3"].append(data["data"]["game"]["teamOne"][2]["summonerId"])
    stat["team1"]["player4"].append(data["data"]["game"]["teamOne"][3]["summonerId"])
    stat["team1"]["player5"].append(data["data"]["game"]["teamOne"][4]["summonerId"])
    stat["team2"]["player1"].append(data["data"]["game"]["teamTwo"][0]["summonerId"])
    stat["team2"]["player2"].append(data["data"]["game"]["teamTwo"][1]["summonerId"])
    stat["team2"]["player3"].append(data["data"]["game"]["teamTwo"][2]["summonerId"])
    stat["team2"]["player4"].append(data["data"]["game"]["teamTwo"][3]["summonerId"])
    stat["team2"]["player5"].append(data["data"]["game"]["teamTwo"][4]["summonerId"])

    # SummonerInternalName
    # Reference for champion ID
    stat["team1"]["player1"].append(data["data"]["game"]["teamOne"][0]["summonerInternalName"])
    stat["team1"]["player2"].append(data["data"]["game"]["teamOne"][1]["summonerInternalName"])
    stat["team1"]["player3"].append(data["data"]["game"]["teamOne"][2]["summonerInternalName"])
    stat["team1"]["player4"].append(data["data"]["game"]["teamOne"][3]["summonerInternalName"])
    stat["team1"]["player5"].append(data["data"]["game"]["teamOne"][4]["summonerInternalName"])
    stat["team2"]["player1"].append(data["data"]["game"]["teamTwo"][0]["summonerInternalName"])
    stat["team2"]["player2"].append(data["data"]["game"]["teamTwo"][1]["summonerInternalName"])
    stat["team2"]["player3"].append(data["data"]["game"]["teamTwo"][2]["summonerInternalName"])
    stat["team2"]["player4"].append(data["data"]["game"]["teamTwo"][3]["summonerInternalName"])
    stat["team2"]["player5"].append(data["data"]["game"]["teamTwo"][4]["summonerInternalName"])
    
    # Summoner champions

    for x in range(len(data["data"]["game"]["playerChampionSelections"])):
      
      internalname = data["data"]["game"]["playerChampionSelections"][x]["summonerInternalName"]
      champID = data["data"]["game"]["playerChampionSelections"][x]["championId"]        
      
      if internalname in stat["team1"]["player1"]:      
        stat["team1"]["player1"].append(champID)      
      if internalname in stat["team1"]["player2"]:      
        stat["team1"]["player2"].append(champID)         
      if internalname in stat["team1"]["player3"]:      
        stat["team1"]["player3"].append(champID)    
      if internalname in stat["team1"]["player4"]:      
        stat["team1"]["player4"].append(champID)       
      if internalname in stat["team1"]["player5"]:      
        stat["team1"]["player5"].append(champID)         
      if internalname in stat["team2"]["player1"]:      
        stat["team2"]["player1"].append(champID)
      if internalname in stat["team2"]["player2"]:      
        stat["team2"]["player2"].append(champID)
      if internalname in stat["team2"]["player3"]:      
        stat["team2"]["player3"].append(champID)         
      if internalname in stat["team2"]["player4"]:      
        stat["team2"]["player4"].append(champID)
      if internalname in stat["team2"]["player5"]:      
        stat["team2"]["player5"].append(champID)  

    # Pull Player Levels
    response = unirest.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/" + str(stat["team1"]["player1"][1]) + ","  + str(stat["team1"]["player2"][1]) + ","  + str(stat["team1"]["player3"][1]) + ","  + str(stat["team1"]["player4"][1]) + ","  + str(stat["team1"]["player5"][1]) + ","  + str(stat["team2"]["player1"][1]) + ","  + str(stat["team2"]["player2"][1]) + ","  + str(stat["team2"]["player3"][1]) + ","  + str(stat["team2"]["player4"][1]) + ","  + str(stat["team2"]["player5"][1]) + "?api_key=409d8cdd-8129-4541-b34e-d7c61dee9658")
    data = response.body
    
    # Summonor Levels
    try:
      stat["team1"]["player1"].append(data[str(stat["team1"]["player1"][1])]["summonerLevel"])
    except:
      stat["team1"]["player1"].append(-999)
    try:
      stat["team1"]["player2"].append(data[str(stat["team1"]["player2"][1])]["summonerLevel"])
    except:
      stat["team1"]["player2"].append(-999)
    try:
      stat["team1"]["player3"].append(data[str(stat["team1"]["player3"][1])]["summonerLevel"])
    except:
      stat["team1"]["player3"].append(-999)
    try:
      stat["team1"]["player4"].append(data[str(stat["team1"]["player4"][1])]["summonerLevel"])
    except:
      stat["team1"]["player4"].append(-999)
    try:
      stat["team1"]["player5"].append(data[str(stat["team1"]["player5"][1])]["summonerLevel"])
    except:
      stat["team1"]["player5"].append(-999)
    try:
      stat["team2"]["player1"].append(data[str(stat["team2"]["player1"][1])]["summonerLevel"])
    except:
      stat["team2"]["player1"].append(-999)
    try:
      stat["team2"]["player2"].append(data[str(stat["team2"]["player2"][1])]["summonerLevel"])
    except:
      stat["team2"]["player2"].append(-999)
    try:
      stat["team2"]["player3"].append(data[str(stat["team2"]["player3"][1])]["summonerLevel"])
    except:
      stat["team2"]["player3"].append(-999)
    try:
      stat["team2"]["player4"].append(data[str(stat["team2"]["player4"][1])]["summonerLevel"])
    except:
      stat["team2"]["player4"].append(-999)
    try:
      stat["team2"]["player5"].append(data[str(stat["team2"]["player5"][1])]["summonerLevel"])
    except:
      stat["team2"]["player5"].append(-999)
    print("ready to write")
    datasave.save(stat,"data/teaminfo.dat")

    # Pull Champ Names
    response = unirest.get("https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(stat["team1"]["player1"][2]) + "?api_key=409d8cdd-8129-4541-b34e-d7c61dee9658")
    data = response.body
    stat["team1"]["player1"].append(data["name"])
    response = unirest.get("https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(stat["team1"]["player2"][2]) + "?api_key=409d8cdd-8129-4541-b34e-d7c61dee9658")
    data = response.body
    stat["team1"]["player2"].append(data["name"])
    response = unirest.get("https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(stat["team1"]["player3"][2]) + "?api_key=409d8cdd-8129-4541-b34e-d7c61dee9658")
    data = response.body
    stat["team1"]["player3"].append(data["name"])
    response = unirest.get("https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(stat["team1"]["player4"][2]) + "?api_key=409d8cdd-8129-4541-b34e-d7c61dee9658")
    data = response.body
    stat["team1"]["player4"].append(data["name"])
    response = unirest.get("https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(stat["team1"]["player5"][2]) + "?api_key=409d8cdd-8129-4541-b34e-d7c61dee9658")
    data = response.body
    stat["team1"]["player5"].append(data["name"])

  else:
    print("ready to write")
    datasave.save(["nogame"],"data/teaminfo.dat")


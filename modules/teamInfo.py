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
    stat["team1"]["player1"].append(data["data"]["game"]["teamOne"][0]["accountId"])
    stat["team1"]["player2"].append(data["data"]["game"]["teamOne"][1]["accountId"])
    stat["team1"]["player3"].append(data["data"]["game"]["teamOne"][2]["accountId"])
    stat["team1"]["player4"].append(data["data"]["game"]["teamOne"][3]["accountId"])
    stat["team1"]["player5"].append(data["data"]["game"]["teamOne"][4]["accountId"])
    stat["team2"]["player1"].append(data["data"]["game"]["teamTwo"][0]["accountId"])
    stat["team2"]["player2"].append(data["data"]["game"]["teamTwo"][1]["accountId"])
    stat["team2"]["player3"].append(data["data"]["game"]["teamTwo"][2]["accountId"])
    stat["team2"]["player4"].append(data["data"]["game"]["teamTwo"][3]["accountId"])
    stat["team2"]["player5"].append(data["data"]["game"]["teamTwo"][4]["accountId"])

    # Pull Player Levels
    response = unirest.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/" + str(stat["team1"]["player1"][1]) + ","  + str(stat["team1"]["player2"][1]) + ","  + str(stat["team1"]["player3"][1]) + ","  + str(stat["team1"]["player4"][1]) + ","  + str(stat["team1"]["player5"][1]) + ","  + str(stat["team2"]["player1"][1]) + ","  + str(stat["team2"]["player2"][1]) + ","  + str(stat["team2"]["player3"][1]) + ","  + str(stat["team2"]["player4"][1]) + ","  + str(stat["team2"]["player5"][1]) + "?api_key=d688cd48-fc0d-4cb5-b22b-7a376be8a109",
      headers={
        "X-Mashape-Key": "cr1TQBbsvzmshKj7odQmhnN9xkFep149Dttjsnqs3Af4zb6rQH"
      }
    )
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
      stat["team2"]["player1"].append(data[str(stat["team1"]["player1"][1])]["summonerLevel"])
    except:
      stat["team2"]["player1"].append(-999)
    try:
      stat["team2"]["player2"].append(data[str(stat["team1"]["player2"][1])]["summonerLevel"])
    except:
      stat["team2"]["player2"].append(-999)
    try:
      stat["team2"]["player3"].append(data[str(stat["team1"]["player3"][1])]["summonerLevel"])
    except:
      stat["team2"]["player3"].append(-999)
    try:
      stat["team2"]["player4"].append(data[str(stat["team1"]["player4"][1])]["summonerLevel"])
    except:
      stat["team2"]["player4"].append(-999)
    try:
      stat["team2"]["player5"].append(data[str(stat["team1"]["player5"][1])]["summonerLevel"])
    except:
      stat["team2"]["player45"].append(-999)

    return(stat)
  return(["nogame"])





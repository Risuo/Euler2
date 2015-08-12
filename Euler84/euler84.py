import random
import time

chance = ["GO", 10, 11, 24, 39, 5, "NextRR", "NextRR", "NextUtil", -3, 0, 0, 0, 0, 0, 0]
random.shuffle(chance)

communityChest = ["GO", 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
random.shuffle(communityChest) 

board = {0:{"square": "GO", "count": 0}, 1:{"square": "A1", "count": 0}, 2:{"square":"CC1", "count": 0}, 3:{"square":"A2", "count":0}, 
        4:{"square":"T1", "count":0}, 5:{"square":"R1", "count":0}, 6:{"square":"B1", "count":0}, 7:{"square":"Chance1", "count":0}, 
        8:{"square":"B2", "count":0}, 9:{"square":"B3", "count":0}, 10:{"square":"JAIL", "count":0} , 11:{"square":"C1", "count":0},
        12:{"square":"Util1", "count":0}, 13:{"square":"C2", "count":0}, 14:{"square":"C3", "count":0}, 15:{"square":"R2", "count":0},
        16:{"square":"D1", "count":0}, 17:{"square":"CC2", "count":0}, 18:{"square":"D2", "count":0}, 19:{"square":"D3", "count":0}, 
        20:{"square":"FP", "count":0}, 21:{"square":"E1", "count":0}, 22:{"square":"Chance2", "count":0}, 23:{"square":"E2", "count":0},
        24:{"square":"E3", "count":0}, 25:{"square":"R3", "count":0}, 26:{"square":"F1", "count":0}, 27:{"square":"F2", "count":0},
        28:{"square":"Util2", "count":0}, 29:{"square":"F3", "count":0}, 30:{"square":"GOTOJAIL", "count":0}, 31:{"square":"G1","count":0},
        32:{"square":"G2", "count":0}, 33:{"square":"CC3", "count":0}, 34:{"square":"G3", "count":0}, 35:{"square":"R4", "count":0},
        36:{"square":"Chance3", "count":0}, 37:{"square":"H1", "count":0}, 38:{"square":"T2", "count":0}, 39:{"square":"H2", "count":0}}

def diceRoll():
  return random.randrange(1,5), random.randrange(1,5)  

def CommunityChest(comChestCardCount):
  if communityChest[comChestCardCount] == "GO":
    return "GO"
  else: 
    return communityChest[comChestCardCount]
  
def Chance(cardCount, location):
  if location == "Chance1":
    if chance[cardCount] == "NextRR":
      return 15
    if chance[cardCount] == "NextUtil":
      return 12
    if chance[cardCount] == -3:
      return 4
    if chance[cardCount] == "GO":
      return "GO"
    else:
      return chance[cardCount]
  if location == "Chance2":
    if chance[cardCount] == "NextRR":
      return 25
    if chance[cardCount] == "NextUtil":
      return 28
    if chance[cardCount] == -3:
      return 19
    if chance[cardCount] == "GO":
      return "GO"
    else:
      return chance[cardCount]
  if location == "Chance3":
    if chance[cardCount] == "NextRR":
      return 5
    if chance[cardCount] == "NextUtil":
      return 12
    if chance[cardCount] == -3:
      return -3
    if chance[cardCount] == "GO":
      return "GO"
    else:
      return chance[cardCount]

#print Chance(9, "Chance3", chance, 5)

def runGame(turns):
  location = 0
  doubleCount = 0
  cardCount = 0
  comChestCardCount = 0
  for x in xrange(1, turns): 
    dice = diceRoll()
    roll = sum(dice)
    if dice[0] == dice[1]:
      doubleCount += 1
      if doubleCount <3:
        location += roll
        if location > 39: 
          location -= 40
        if location == 30:
          location = 10
        tile = board[location]["square"]
      if doubleCount == 3:
        location = 10
        tile = board[location]["square"]
        doubleCount = 0
    else:
      doubleCount = 0
      location += roll
      if location > 39: 
        location -= 40
      if location == 30:
        location = 10
      tile = board[location]["square"]
    if str(tile) == "CC1" or str(tile) == "CC2" or str(tile) == "CC3": 
      cardDraw = CommunityChest(comChestCardCount)
      comChestCardCount += 1
      #print 'this is the community chest card drawn:', cardDraw, 'from this square:', tile
      if comChestCardCount == 16:
        comChestCardCount = 0
      if cardDraw == "GO":
        location = 0
        tile = board[location]["square"]
      elif cardDraw == 10:
        location = 10
        tile = board[location]["square"]
      else:
        tile = board[location]["square"]
    if str(tile) == "Chance1" or str(tile) == "Chance2" or str(tile) == "Chance3":
      cardDraw = Chance(cardCount, tile)
      #print 'this is the chance card drawn:', cardDraw, 'from this square:', tile
      cardCount += 1
      if cardCount == 16:
        cardCount = 0
      if cardDraw == 'GO':
        location = 0
        tile = board[location]["square"]
      elif cardDraw == 0:
        tile = board[location]["square"]
      elif cardDraw == 10:
        location = 10
        tile = board[location]["square"]
      elif str(tile) == "Chance3" and cardDraw == -3:
        cardDraw = CommunityChest(comChestCardCount)
        #print 'and since it was Chance3 and -3, we drew a community chest card, which was:', cardDraw
        comChestCardCount += 1
        if comChestCardCount == 16:
          comChestCardCount = 0
        if cardDraw == "GO":
          location = 0
          tile = board[location]["square"]
        elif cardDraw == 0:
          tile = board[location]["square"]
        elif cardDraw == 10:
          location = 10
          tile = board[location]["square"]
        else:
          tile = board[location]["square"]
      elif str(tile) != "Chance3" and cardDraw == -3:
        tile = board[location-3]["square"]
      else:
        location = int(cardDraw)
        tile = board[location]["square"]
    board[location]["count"] += 1
    #print tile, roll, 'turn:', x, board[location]["count"]  
  return board
start = time.time() 
endGame = runGame(7000000)
elapsed = time.time() - start
print elapsed
total = 0
squareCount = []
start = time.time()
for x in endGame:
  squareCount.append([endGame[x]["count"], endGame[x]["square"]])
squareCount.sort()
squareCount.reverse()
elapsed = time.time() - start
print squareCount[:7] 
print elapsed 

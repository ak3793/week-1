import random

class Player:
    I = 0
    P = 0
    C = 0
    
    def __init__(self, inputID, startingPot):
        self.P = inputID
        self.I = startingPot
        
    def play(self, dealerCard):
        self.C = random.choice(cards)
        
        if self.C < dealerCard:
            self.I -= gameStake
            return 'player ' + str(self.P) + ' Lose:' + str(self.C) + ' vs ' + str(dealerCard)
        else:
            self.I += gameStake
            return 'player ' + str(self.P) + ' Wins: ' + str(self.C) + ' vs ' + str(dealerCard)
        
    def returnPot(self):
        return self.I
        
    def returnID(self):
        return self.P


def playHand(players):
    
    for player in players:
        print player.play(random.choice(cards))
        
def checkBalances(players):
    
    for player in players:
        print 'player ' + str(player.returnID()) + ' has $' + str(player.returnPot()) + ' left.'

gameStake = 50  
cards = range(10)

players = []

for i in range(5):
    players.append(Player(i, 1000))

for i in range(5):
    print 'start game ' + str(i)
    playHand(players)

print 'GAME RESULTS:'
checkBalances(players)




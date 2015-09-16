import random
game = 0
totalSum =[]
x = 0
y = 50
tS = []
while game < 10:
    print "Start game"+ str(game)
    for i in range(5):
    	pl = random.randint(0,9)
    	dl = random.randint(0,9)
    	if pl<dl:
                print ' player ' + str(i) + " loses " + str(pl) + " vs " + str(dl)
                x = (False)
        else:
            print ' player ' + str(i) + " wins " + str(pl) + " vs " + str(dl)
            x = (True)
        if x:
            y = y + 10
            tS.append(y)
        else:
            y = y - 10
            tS.append(y)
                         
    game += 1 
    
print "Game Results"
for n in range(5):
    print "player" + str(n) + " has $ " + str(tS)+ " left "
    
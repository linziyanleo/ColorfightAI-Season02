# You need to import colorfight for all the APIs
import colorfight
import random

if __name__ == '__main__':
    g = colorfight.Game()
    if g.JoinGame('Magikarp'):
        while True:
            for x in range(g.width):
                for y in range(g.height):
                    c = g.GetCell(x,y)
                    if c.owner == g.uid:
                        # Pick a random direction based on current cell 
                        d = random.choice([(0,1), (0,-1), (1, 0), (-1,0)])
                        # Get that adjacent cell
                        cc = g.GetCell(x+d[0], y+d[1])
                        if cc != None:
                            if cc.owner != g.uid:
                                print(g.AttackCell(x+d[0], y+d[1]))
                                g.Refresh()
    else:
        print ("Failed to join the game!")

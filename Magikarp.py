import colorfight
import random

class ai:
    def __init__(self):
        self.game = colorfight.Game()
        self.game.JoinGame('Magikarp')

    def main(self):
        AttackList = []
        while True:
            #game.AttackCell(AttackList[-1])
            #AttackList.pop(-1)
            for x in range(game.width):
                for y in range(game.height):
                    c = game.GetCell(x, y)
                    if c.owner == game.uid:
                        d = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
                        cc = game.GetCell(x + d[0], y + d[1])
                        if cc != None:
                            if cc.owner != game.uid:
                                print(game.AttackCell(x + d[0], y + d[1]))
                                game.Refresh()
        else:
            print("Failed to join the game!")

    def CanAttack(self):
        AttackList = []
        myCell = self.my_cell()
        for cell in myCell

A = ai()
A.main()
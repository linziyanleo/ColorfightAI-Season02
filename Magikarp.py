import colorfight
import random
from operator import itemgetter

class ai:
    def __init__(self):
        self.g = colorfight.Game()
        self.g.JoinGame('Magikarp')

    def main(self):
        AttackList = []
        while True:
            AttackList = self.CanAttack()
            print(AttackList)
            #G = self.gold(AttackList)
            d = AttackList[0][0]
            print(self.g.AttackCell(d[0], d[1]))
            self.g.Refresh()
            '''
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
            '''
        else:
            print("Failed to join the game!")

    def my_cell(self):
        mycell = []
        for x in range(self.g.width):
            for y in range(self.g.height):
                c = self.g.GetCell(x,y)
                if c.owner == self.g.uid:
                    loc = (str(x),str(y))
                    mycell.append(loc)
        return mycell

    def enemy_cell(self):
        enemycell = []
        for x in range(self.g.width):
            for y in range(self.g.height):
                c = self.g.GetCell(x, y)
                if c.owner == self.g.uid:
                    loc = (str(x), str(y))
                    enemycell.append(loc)
        return enemycell

    def CanAttack(self):
        AttackList = []
        emptyCell = []
        myCell = self.my_cell()
        for cell in myCell:
            x = int(cell[0])
            y = int(cell[1])
            me = self.g.GetCell(x,y)
            temp = []
            a = self.g.GetCell(x + 1, y)
            b = self.g.GetCell(x - 1, y)
            c = self.g.GetCell(x, y + 1)
            d = self.g.GetCell(x, y - 1)
            pointList = [a, b, c, d]
            for i in range(4):
                if pointList[i] != None:
                    if pointList[i].isTaking == False:
                        if pointList[i].owner != self.g.uid:
                            point = (pointList[i].x, pointList[i].y)
                            if pointList[i].owner == 0:
                                emptyCell.append(point)
                            elif pointList[i].cellType == 'gold':
                                AttackList.append([point, 3.0])
                            else:
                                AttackList.append([point,pointList[i].takeTime])
       # print(AttackList)
        AttackList.sort(key = lambda tup:tup[1])
        return AttackList

    def gold(self,AttackList):
        Attack = []
        for point in AttackList:
            cell = self.g.GetCell(point[0],point[1])
            cell1 = self.g.GetCell(point[0]+1,point[1])
            cell2 = self.g.GetCell(point[0]-1,point[1])
            cell3 = self.g.GetCell(point[0],point[1]+1)
            cell4 = self.g.GetCell(point[0],point[1]-1)
            if cell.cellType == 'gold':
                AttackList.append(point,cell.takeTime-0.4)
            elif cell1.cellType == 'gold' or cell2.cellType == 'gold' or cell3.cellType == 'gold' or cell4.cellType == 'gold':
                AttackList.append(point,cell.takeTime-0.25)
        AttackList.sort(key=lambda tup: tup[1])
        return AttackList

    #def getAround(self,x,y):
'''
if pointList[i].owner == 0:
    emptyCell.append(point)
elif pointList[i].cellType == 'gold':
    AttackList.append([point, 3.02])
else:


    def agressive(self):
        enemy = self.enemy_cell()
        if 

    def eatCorner(self):
'''
A = ai()
A.main()
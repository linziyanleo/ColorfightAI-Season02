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
            AttackList = self.listWeight()
            print(AttackList)
            #G = self.gold(AttackList)
            d = AttackList[0][0]
            if AttackList[0][1] <= 0:
                d = AttackList[1][0]
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
                if c.owner != self.g.uid:
                    loc = (str(x), str(y))
                    enemycell.append(loc)
        return enemycell

    def CanAttack(self,myCell):
        AttackList = []
        emptyCell = []
        #print(myCell)
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
            print(pointList)
            for i in range(4):
                if pointList[i] != None:
                    if pointList[i].isTaking == False:
                        if pointList[i].owner != self.g.uid:
                            point = (pointList[i].x, pointList[i].y)
                            if pointList[i].cellType == 'gold' and pointList[i].owner == 0:
                                AttackList.append([point, 1])
                            elif pointList[i].cellType == 'gold' and pointList[i].owner != 0:
                                AttackList.append([point,pointList[i].takeTime - 1.5])
                            else:
                                AttackList.append([point,pointList[i].takeTime])
        AttackList.sort(key = lambda tup:tup[1])
        #print(AttackList)
        return AttackList


    def eatCorner(self,myCell,enemyCell):
        fill = []
        i = 0
        for cell in enemyCell:
            count = 0
            x = int(cell[0])
            y = int(cell[1])
            if (str(x-1),str(y)) in myCell:
                count = count + 1
            if (str(x + 1), str(y)) in myCell:
                count = count + 1
            if (str(x), str(y - 1)) in myCell:
                count = count + 1
            if (str(x), str(y + 1)) in myCell:
                count = count + 1
            if self.g.GetCell(x,y).owner != self.g.uid:
                fill.append((cell,count))
        return fill

    def listWeight(self):
        myCell = self.my_cell()
        enemyCell = self.enemy_cell()
        corner = self.eatCorner(myCell,enemyCell)
        attackable = self.CanAttack(myCell)
        #goldAround = self.goldAround(attackable)
        for point in corner:
            cell = self.g.GetCell(int(point[0][0]),int(point[0][1]))
            if point[1] == 2:
                attackable.append(((int(point[0][0]),int(point[0][1])),cell.takeTime-1.3))
            if point[1] == 3:
                attackable.append(((int(point[0][0]),int(point[0][1])),cell.takeTime-1.7))
            if point[1] == 4:
                attackable.append(((int(point[0][0]),int(point[0][1])),cell.takeTime-1.9))
        attackable.sort(key=lambda tup: tup[1])
        return attackable

    '''
    if pointList[i].owner == 0:
        emptyCell.append(point)
    elif pointList[i].cellType == 'gold':
        AttackList.append([point, 3.02])
    else:


        def agressive(self):
            enemy = self.enemy_cell()
            if 
    '''

'''
    def pointAround(selfx,y):
        Attack = []
        for point in AttackList:
            cell = self.g.GetCell(x,y)
            cellList = []
            for i in range(1,4):
                cell1 = self.g.GetCell(x + i,y)
                cell2 = self.g.GetCell(x - i, y)
                cell3 = self.g.GetCell(x, y - i)
                cell4 = self.g.GetCell(x, y + i)
                cellList.append(cell1)
                cellList.append(cell2)
                cellList.append(cell3)
                cellList.append(cell4)
                #for j in cellList

            if cell.cellType == 'gold':
                AttackList.append(point,cell.takeTime-0.4)
            elif cell1.cellType == 'gold' or cell2.cellType == 'gold' or cell3.cellType == 'gold' or cell4.cellType == 'gold':
                AttackList.append(point,cell.takeTime-0.25)
        AttackList.sort(key=lambda tup: tup[1])
        return AttackList

    #def getAround(self,x,y):
'''

A = ai()
A.main()
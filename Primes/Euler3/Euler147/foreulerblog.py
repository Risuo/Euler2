



class CrossHatched:
    
    def __init__(self, x, y):
        self.columns = x
        self.rows = y
        self.area = self.columns*self.rows
        self.tableA = []
        self.wide = False
        self.tall = False
        self.square = False
        self.crossHatchedOut = []
        if self.rows > self.columns:
            self.tall = True
        if self.columns > self.rows:
            self.wide = True
        if self.columns%2 == 0 and self.rows%2 == 0 and self.columns == self.rows:
            self.odd = False
            self.even = True
        else:
            self.odd = True
            self.even = False
        if self.columns == self.rows:
            self.crossLimit = (self.columns-1)*2
            self.square = True
        if not self.square:
            self.crossLimit = ((min(self.columns, self.rows)-1)*2)+1
            self.square = False

        if self.square:
            for x in xrange(2,self.crossLimit+1,2):
                self.tableA.append(x)
            for x in xrange(self.crossLimit,1,-2):
                self.tableA.append(x)
        else:
            self.difference = max(self.columns,self.rows)-min(self.columns,self.rows)
            for x in xrange(2,self.crossLimit,2):
                self.tableA.append(x)
            for x in xrange(self.difference,1,-1):
                self.tableA.append(self.crossLimit)
            if self.odd:
                self.tableA.append(self.crossLimit)
            self.remainder = self.crossLimit - self.difference
            for x in xrange(self.crossLimit-1,0,-2):
                self.tableA.append(x)

        self.tableMax = max(self.tableA)
        self.dimensionMax = max(self.columns,self.rows)
        self.padMax = max(self.tableMax, self.dimensionMax)

        if self.wide or self.tall:
            self.padLeft = self.rows-2
            self.padRight = self.columns-2

        if self.square:
            self.padLeft = (self.padMax-2)/2
            self.padRight = (self.padMax-2)/2
        
        
        self.tableB = [[] for x in xrange(len(self.tableA))]
        index = -1
        halfLeft = [x for x in xrange(self.padLeft,-1,-1)]
        halfRight = [x for x in xrange(self.padRight,-1,-1)]
        if self.odd or self.square:
            halfLeft.append(0)
            halfRight.append(0)
        elif self.even and not self.square:
            halfLeft.append(0)
            halfLeft.append(0)
            halfRight.append(0)
            halfRight.append(0)
        halfLeft2 = [x for x in xrange(1,self.padRight+1)]
        halfRight2 = [x for x in xrange(1,self.padLeft+1)]
        self.fullLeft = halfLeft + halfLeft2
        self.fullRight = halfRight + halfRight2
        
        for row in self.tableB:
            index += 1
            for value in xrange(self.fullLeft[index]):
                row.append(0)
            for value in xrange(self.tableA[index]):
                row.append(1)
            for value in xrange(self.fullRight[index]):
                row.append(0)
                
            
            self.crossHatchedOut.append(row)



class Grid:
    
    
    
    def __init__(self, table, x, y):
        
        self.columns = x
        self.rows = y
        self.gridMaxSquare = min(self.columns, self.rows)
        self.rowIDtable = []
        self.table = table
        rowID = -1
        for row in self.table:
            rowID += 1
            self.rowIDtable.append(rowID)
        
        self.cellIDtable = []
        
        for rowID in self.rowIDtable:
            self.subRow = []
            index = 0
            reverse = len(self.table[rowID])-1
            if self.table[rowID][0] == 0:
                while self.table[rowID][index] == 0:
                    index += 1
                    self.subRow.append(0)
                self.topLeft = [index,rowID]
            else:
                self.topLeft = [0,rowID]
            if self.table[rowID][-1] == 0:
                while table[rowID][reverse] == 0:
                    reverse -= 1
                self.topRight = [reverse,rowID]
            else:
                self.topRight = [reverse,rowID]
            

            self.maxLength = self.topRight[0]-self.topLeft[0]+1
            self.subRow.append(self.maxLength)
            while index < reverse+1:
                self.maxLength -= 1
                self.subRow.append(self.maxLength)
                if len(self.subRow) == len(self.table[rowID]):
                    index += 5000
                index += 1
            while len(self.subRow) < len(self.table[rowID]):
                self.subRow.append(0)
            self.cellIDtable.append(self.subRow)
        
        
        def cellIndex(cell, row):
            return row.index(cell)


        def horizontal(cellvalue):
            return cellvalue-1
            
        def vertical_Square(rowID, cell, cellIndex, table):
            columnTable = []
            squareOut = 0
            for row in table[rowID+1::]:
                if row[cellIndex] != 0:
                    columnTable.append(row[cellIndex])
            
            size = len(columnTable)
            verticalOut = size

            if size > 0:
                for cell2 in columnTable:
                    squareOut += min(cell2, cell)-1
                

            return squareOut + verticalOut
        
        self.H = 0
        self.V_S = 0
        self.C = 0
        rowID = -1
        for row2 in self.cellIDtable:
            rowID += 1
            for cell2 in row2:
                if cell2 == 0:
                    continue
                cellindex = cellIndex(cell2,row2)
                self.H += horizontal(cell2)
                self.V_S += vertical_Square(rowID, cell2, cellindex, self.cellIDtable)
                self.C += 1
        
        

        
def rectangleCount(x,y):
    return((y*(y+1)*x*(x+1))/4)
        

def run(x,y):
    totalRectangles = 0
    for x in xrange(1,x+1):
        for y in xrange(1,y+1):
            reg = rectangleCount(x,y)
            if x >= 2 or y >= 2:
                
                test = CrossHatched(x,y)
                crossHatchedTable = test.crossHatchedOut
                
                
                gridTest = Grid(crossHatchedTable, x, y)
                totalRectangles += (gridTest.H + gridTest.V_S + gridTest.C + reg)
            
            else:
                totalRectangles += (reg + max(x,y)-1)

            
    return totalRectangles
            
print run(47,43)




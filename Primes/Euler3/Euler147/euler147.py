

class CrossHatched: # This class only handles grids of either dimension being at least 2. There will need to be a separate
                    # solving for grids with at least one dimension = 1 (but it's going to be really straightforward, because it's just a single row or column)
    
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
            #print self.crossLimit
            for x in xrange(2,self.crossLimit+1,2):
                self.tableA.append(x)
            for x in xrange(self.crossLimit,1,-2):
                self.tableA.append(x)
        else:
            #print self.crossLimit
            self.difference = max(self.columns,self.rows)-min(self.columns,self.rows)
            for x in xrange(2,self.crossLimit,2):
                self.tableA.append(x)
                #print 'adding', x
            for x in xrange(self.difference,1,-1):
                self.tableA.append(self.crossLimit)
                #print 'adding @2', self.crossLimit
            if self.odd:
                self.tableA.append(self.crossLimit)
                #print 'adding @3', self.crossLimit
            self.remainder = self.crossLimit - self.difference
            for x in xrange(self.crossLimit-1,0,-2):
                self.tableA.append(x)
                #print 'adding @4', x

        self.tableMax = max(self.tableA)
        self.dimensionMax = max(self.columns,self.rows)
        #self.gridMax = len(self.tableA)+1
        self.padMax = max(self.tableMax, self.dimensionMax)#, self.gridMax)
        #if self.dimensionMax > self.tableMax:
        #    self.padMax = self.dimensionMax
            #print 'padMax = dimensionmax =', self.padMax
        #else:
        #    self.padMax = self.tableMax
            #print 'paxMax = tableMax =', self.padMax
        if self.wide or self.tall:
            self.padLeft = self.rows-2
            self.padRight = self.columns-2
        #if self.tall:
        #    self.padLeft = self.rows-2
        #    self.padRight = self.columns-2
        if self.square:
            self.padLeft = (self.padMax-2)/2
            self.padRight = (self.padMax-2)/2
        
        
        self.tableB = [[] for x in xrange(len(self.tableA))]
        index = -1
        #print self.padLeft, self.padRight
        halfLeft = [x for x in xrange(self.padLeft,-1,-1)]
        halfRight = [x for x in xrange(self.padRight,-1,-1)]
        #print halfLeft, halfRight, 'half left/right before appending zeros'
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
        
        #print self.tableA, 'wide:', self.wide, 'tall:', self.tall, 'square:', self.square
        #print self.padLeft, self.padRight, self.padMax, 'first set'
        
        #print self.fullLeft, self.fullRight, 'second set'
        #print self.tableB, 'third set'
        
        for row in self.tableB:
            index += 1
            for value in xrange(self.fullLeft[index]):
                row.append(0)
            for value in xrange(self.tableA[index]):
                row.append(1)
            for value in xrange(self.fullRight[index]):
                row.append(0)
                
            
            self.crossHatchedOut.append(row)
            #print row


class Grid:
    
    
    def __init__(self, table, x, y): # Use    Grid(example.crossHatchedOut)
        
        self.columns = x
        self.rows = y
        self.gridMaxSquare = min(self.columns, self.rows)
        self.rowIDtable = []
        self.table = table
        rowID = -1
        for row in self.table:
            rowID += 1
            self.rowIDtable.append(rowID)
        
        
        # Need to work on the identification here
        self.cellIDtable = []
        
        for rowID in self.rowIDtable:
            self.subRow = []
            index = 0
            reverse = len(self.table[rowID])-1
            #print self.table[rowID], 'this is the row being worked on'
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
            #for cell in table[rowID]:            #    print cell
            

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
            #print 'here are the variables within the vertical call:', rowID, 'rowID', cell, 'cell', cellIndex, 'cellIndex', table, 'table'
            for row in table[rowID+1::]:
                if row[cellIndex] != 0:
                    columnTable.append(row[cellIndex])
            
            size = len(columnTable)
            verticalOut = size

            if size > 0:
                #print cell, columnTable, 'cell and columnTable'
                for cell2 in columnTable:
                    squareOut += min(cell2, cell)-1
                
            
            #print squareOut, '<-- squareOut, verticalOut -->', verticalOut
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
                self.H += horizontal(cell2)#, 'horizontal test for cell:', cell2, 'in row:', row2
                self.V_S += vertical_Square(rowID, cell2, cellindex, self.cellIDtable)#, 'vertical test for cell:', cell2, 'in row:', row2, 'in table:', self.cellIDtable
                self.C += 1
        
        
        
            #print row2 #, len(row2)
        #print self.cellIDtable, 'cellIDtable test'
        

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
                
            

            
                # This is where the Grid class should be utilized, after the table has been created
                # The table format is a 2 dimensional 0/1 matrix, with each row of the table having 1's for valid cells, and 0's for
                # absent, or 'padding' cells for use within the cross-hatched grid creation. Standard rectangles get a formula (yey)
            
                gridTest = Grid(crossHatchedTable, x, y)
                #print 'total rectangles in a', x, 'by', y, 'cross-hatched grid is ===>', gridTest.H + gridTest.V_S + gridTest.C + reg
                totalRectangles += (gridTest.H + gridTest.V_S + gridTest.C + reg)
                #print totalRectangles
            
            else:
                #print 'total rectangles in a', x, 'by', y, 'cross-hatched grid is ===>', reg + max(x,y)-1
                totalRectangles += (reg + max(x,y)-1)
                #print totalRectangles
            
    return totalRectangles


print run(47,43)

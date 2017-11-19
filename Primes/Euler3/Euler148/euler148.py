class PascalDivisibleSeven:
    
    def __init__(self, rows):
        
        
        def fullTriangles(n):
            return (n*(n+1))/2
        
        if self.partialRows > 0:
            self.partialSets = self.fullTriangleSets+1
            if self.partialRows == 1:
                self.partialTriangles = 6*self.partialSets
            if self.partialRows == 2:
                self.partialTriangles = (6+5)*self.partialSets
            if self.partialRows == 3:
                self.partialTriangles = (6+5+4)*self.partialSets
            if self.partialRows == 4:
                self.partialTriangles = (6+5+4+3)*self.partialSets
            if self.partialRows == 5:
                self.partialTriangles = (6+5+4+3+2)*self.partialSets
        if self.partialRows == 0:
            self.partialTriangles = 0
        
        
        
        
rows = 100

test = PascalDivisibleSeven(rows)



class CreateMap:

    def __init__(self, width, height):
        self.map = [[0 for i in xrange(width)] for j in xrange(height)]
        for i in xrange(1,width -1):
            for j in xrange(1, height-1):
                self.map[j][i] = 1

    def printMap(self):
        for line in self.map:
            print line

    def createWalls(self, start, end):
        pos = start
        while pos != end:
            self.map[pos[0]][pos[1]] = 0
            pos = self.getMinNeighbor(pos,end)
            print pos

    def getMinNeighbor(self, pos, end):
        directs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        dist = self.getDistance(pos, end)
        closest = pos
        for dir in directs:
            neighb = [pos[0]+dir[0], pos[1] + dir[1]]
            if self.getDistance(neighb, end) < dist:
                dist = self.getDistance(neighb, end)
                closest = neighb
        return closest



    def getMap(self):
        return self.map

    def getDistance(self, start, end):
        d = abs(start[0] - end[0]) + abs(start[1] - end[1])
        return d




map = CreateMap(10,10)
map.printMap()
map.createWalls([2,3],[5,8])
map.printMap()



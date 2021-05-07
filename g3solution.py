def solution(src, dest):
    #knight move from i to j
    #soln
    move_set = [[-2,-1], [2, -1], [-2, 1], [1, 2]]#, [-1,-2],[1, -2], [-1,2], [2,1]] #all moves can be transposed
    rows = []
    row = []
    unvisited = [] #dijkstra style
    x = 0   # answer
    #coords for src and dest
    o_x = -1
    o_y = -1
    d_x = -1
    d_y = -1
    j = 0
    for i in range(0,64):
        if i == src:
            o_x = i%8
            o_y = j
        elif i == dest:
            d_x = i%8
            d_y = j
        row.append(square(i%8, j))
        if len(row) == 8:
            rows.append(row)
            row = []
            j += 1
    for r in rows:
        for s in r:
            unvisited.append(s)
            getMoves(s, move_set, rows)
    rows[o_x][o_y].set_dst(0) #set src to have dist 0
    if (src == dest):
        x = 0
    else:
        x = search(rows[o_x][o_y], rows[d_x][d_y], unvisited)
    return x

def getMoves(s, moves, board):
    for m in moves:
        x = s.x + m[0]
        y = s.y + m[1]
        if (x >= 0 and x <= 7) and (y >= 0 and y <= 7):
            s.add_square(board[y][x])
        x = s.x + m[1]
        y = s.y + m[0]
        if (x >= 0 and x <= 7) and (y >= 0 and y <= 7):
            s.add_square(board[y][x])

def search(sq, dest, unvisited):
    c_reachable = [s for s in sq.get_reachable() if s in unvisited]
    for s in c_reachable:
        if s in unvisited:
            c_dist = sq.dist + 1
            if c_dist < s.dist:
                s.set_dst(c_dist)
    unvisited.remove(sq)
    if not dest in unvisited:
        return dest.dist
    else:
        min_sq = unvisited[0]
        for uv in unvisited:
            if uv.dist < min_sq.dist:
                min_sq = uv
        search(min_sq, dest, unvisited)
    return dest.dist

class square:

    def __init__(self, x, y):
        self.valid_squares = [] #squares this knight can move to
        self.x = x
        self.y = y
        self.dist = 100

    def getname(self):
        return "({self.x}, {self.y})".format(self=self)

    def __str__(self):
        t = ""
        for s in self.valid_squares:
            t += "{a}".format(a= s.getname())
        return "({self.x}, {self.y}): {sss}".format(self=self, sss = t)

    def set_dst(self, d):
        self.dist = d

    def add_square(self, sq):
        self.valid_squares.append(sq)

    def get_reachable(self):
        return self.valid_squares

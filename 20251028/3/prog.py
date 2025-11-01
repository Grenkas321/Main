class Maze:
    def __init__(self, n=1):
        self.n = n
        self.lab = [["█" for i in range(2 * n + 1)]  for j in range(2 * n + 1)]
        for i in range(n):
            for j in range(n):
                self.lab[2 * i + 1][2 * j + 1] = '·'

    def is_path(self, x, y, tail):
        new_coord = set()
        copy = Maze(self.n)
        copy.lab = [[j for j in i] for i in self.lab]
        if self.lab[y * 2 + 1][x * 2] == '·':
            if (x - 1, y) not in tail:
                tail.add((x - 1, y))
                new_coord = new_coord.union(self.is_path(x - 1, y, tail))
        if self.lab[y * 2 + 1][(x + 1) * 2] == '·':
            if (x + 1, y) not in tail:
                tail.add((x + 1, y))
                new_coord = new_coord.union(self.is_path(x + 1, y, tail))
        if self.lab[y * 2][x * 2 + 1] == '·':
            if (x, y - 1) not in tail:
                tail.add((x, y - 1))
                new_coord = new_coord.union(self.is_path(x, y - 1, tail))
        if self.lab[(y + 1) * 2][x * 2 + 1] == '·':
            if (x, y + 1) not in tail:
                tail.add((x, y + 1))
                new_coord = new_coord.union(self.is_path(x, y + 1, tail))
        return tail.union(new_coord)

    def __getitem__(self, k):
        x0 = k[0]
        y0 = k[1].start
        x1 = k[1].stop
        y1 = k[2]
        coord = self.is_path(x0, y0, set())
        return (x1, y1) in coord

    def __setitem__(self, k, el):
        x0 = k[0]
        y0 = k[1].start
        x1 = k[1].stop
        y1 = k[2]
        x0, x1 = min(x0, x1), max(x0, x1)
        y0, y1 = min(y0, y1), max(y0, y1)
        if y0 == y1:
            for i in range(2 * (x0 + 1), 2 * x1 + 1, 2):
                self.lab[2 * y0 + 1][i] = el
        if x0 == x1:
            for i in range(2 * (y0 + 1), 2 * y1 + 1, 2):
                self.lab[i][2 * x0 + 1] = el
        return el

    def __repr__(self):
        return '\n'.join([''.join(i) for i in self.lab])

import sys
exec(sys.stdin.read())
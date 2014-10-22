'''Board class for Conway'''
import os


class Board(list):

    '''Square board with cells.'''

    def __init__(self, n):
        list.__init__(self, [[0]*n for _ in range(n)])
        self.size = n

    def is_alive(self, row, col):
        '''Returns state of current cell'''
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return 0
        return self[row][col]

    def num_neighs(self, row, col):
        '''Returns number of neighbours of current cell'''
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if row+i < 0 or row+i >= self.size or col+j < 0 or col+j >= self.size:
                    continue
                count += self[row+i][col+j]
        return count

    def next_state(self, row, col):
        '''Returns next state for a paticular cell'''
        neighs = self.num_neighs(row, col)
        return int((neighs == 3 or
                    (self[row][col] and neighs == 2)))

    def next_board(self):
        '''Updates all cells in the board'''
        next_board = Board(self.size)
        for i in range(self.size):
            for j in range(self.size):
                next_board[i][j] = self.next_state(i, j)
        return next_board

    def __repr__(self):
        os.system('clear')
        string = ""
        for row in self:
            for col in row:
                if col:
                    string += '.'
                else:
                    string += ' '

            string += '\n'
        return string + ''.join(['_']*self.size)

    def color(self, i, j, step):
        '''Chooses a color depending on number of neighbours'''
        neighs = self.num_neighs(i, j)
        new_color = (255, 255, 255)
        if neighs == 1:
            new_color = (min(255, 256-step), 255, 0)
        if neighs == 2:
            new_color = (min(255, 256-step), 200, 0)
        if neighs == 3:
            new_color = (min(255, 256-step), 150, 50)
        if neighs == 4:
            new_color = (min(255, 256-step), 100, 50)
        if neighs == 5:
            new_color = (min(255, 256-step), 50, 50)
        if neighs == 6:
            new_color = (0, 0, 0)
        return new_color

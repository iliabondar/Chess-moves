from ChessPiece import ChessPiece
#  конь
#  +2 и +1; два варианта попасть в одну клетку
class ChessPieceHorse(ChessPiece):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)
        self.name = 'Конь'
        self.position_x = position_x
        self.position_y = position_y

    def number_of_possible_moves(self, size_x, size_y):

        if ((self.position_x <= 0) or (self.position_x >= size_x)) and ((self.position_y <= 0) or (self.position_y >= size_y)):
            print('в этой клетке у ' + self.name + ' есть 4 хода')

        if (((0 < self.position_x <= 1) or (size_x-1 <= self.position_x < size_x)) and (self.position_y <= 0)) \
                or (((0 < self.position_y <= 1) or (size_y-1 <= self.position_y < size_y)) and (self.position_x <= 0)):
            print('в этой клетке у ' + self.name + ' есть 6 ходов')

        if ((0 < self.position_x <= 1) or (size_x-1 <= self.position_x < size_x)) \
                and ((0 <= self.position_y <= 1) or (size_y-1 <= self.position_y < size_y)):
            print('в этой клетке у ' + self.name + ' есть 8 ходов')

        if (((2 <= self.position_x < 3) or (size_x - 2 <= self.position_x < size_x-1)) and (0 < self.position_y <= 1)) \
            or (((2 <= self.position_y < 3) or (size_y - 2 <= self.position_y < size_y-1)) and (0 < self.position_x <= 1)):
            print('в этой клетке у ' + self.name + ' есть 12 ходов')

        if (size_x -2 >= self.position_x >= 2) and (size_y-2 >= self.position_y >= 2):
            print('в этой клетке у ' + self.name + ' есть 16 ходов')
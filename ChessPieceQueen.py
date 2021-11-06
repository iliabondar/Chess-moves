from ChessPiece import ChessPiece
#Королева
class ChessPieceQueen(ChessPiece):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)
        self.name = 'Ферзь'
        self.position_x = position_x
        self.position_y = position_y
# от (x,y) до минимума из двух значений по диагонали; по прямой от (x,y) до конца поля
    def number_of_possible_moves (self, size_x, size_y):
        return min(self.position_x, self.position_y) + min(self.position_x, size_y - self.position_y - 1) \
               + min(size_y - self.position_y - 1, size_x - self.position_x - 1) \
               + min(size_x - self.position_x - 1, self.position_y) + size_x-1 + size_y - 1
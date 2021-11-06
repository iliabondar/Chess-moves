from ChessPiece import ChessPiece
# пешка
# по прямой от (x,y) до size_y
class ChessPiecePawn ( ChessPiece ):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)
        self.name = 'Пешка'
        self.position_x = position_x
        self.position_y = position_y
    def number_of_possible_moves (self, size_x, size_y):
        if (self.position_y<size_y):
            print('в этой клетке у '+self.name+ ' имеет 1 ход')
        else:
            print ('в этой клетке '+self.name+' не имеет ходов')
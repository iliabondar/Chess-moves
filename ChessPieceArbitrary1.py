# произвольная фигура
# на верхней половине доски ходит на 3 по диагонали
# на нижней половине по прямой на 4
from ChessPiece import ChessPiece
class ChessPieceArbitrary (ChessPiece):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)
        self.name = 'Произвольная шахматная фигура'
        self.position_x = position_x
        self.position_y = position_y

    def number_of_possible_moves(self, size_x, size_y):
        if (size_y) //2 <= self.position_y <= size_y:      # верхняя половина доски (3 диагональ)
            if ((self.position_x>=3) or (self.position_x <= size_x-3)) and (self.position_y <= size_y -3):
                print ('в этой клетке '+self.name+' имеет 12 ходов')

            # убываем по Х
            if (( 2 <= self.position_x < 3) or (size_x -2 <= self.position_x < size_x -2)) and (self.position_y <= size_y -3):
                print('в этой клетке ' + self.name + ' имеет 10 ходов')

            if (( 1 <= self.position_x < 2) or (size_x -1 <= self.position_x < size_x )) and (self.position_y <= size_y -3):
                print('в этой клетке ' + self.name + ' имеет 8 ходов')

            if ((self.position_x < 1) or (size_x -1 < self.position_x)) and (self.position_y <= size_y -3):
                print('в этой клетке ' + self.name + ' имеет 6 ходов')

            # убыаем по Х и У
            if (( 2 <= self.position_x < 3) or (size_x -2 <= self.position_x < size_x -2)) and (size_y -2 <= self.position_y < size_y -1):
                print('в этой клетке ' + self.name + ' имеет 9 ходов')

            if (( 2 <= self.position_x < 3) or (size_x -2 <= self.position_x < size_x -2)) and (size_y -1 <= self.position_y < size_y -1):
                print('в этой клетке ' + self.name + ' имеет 7 ходов')

            if (( 2 <= self.position_x < 3) or (size_x -2 <= self.position_x < size_x -2)) and (size_y <= self.position_y):
                print('в этой клетке ' + self.name + ' имеет 5 ходов')

            #
            if (( 1 <= self.position_x < 2) or (size_x -1 <= self.position_x < size_x )) and (size_y -2 <= self.position_y < size_y -1):
                print('в этой клетке ' + self.name + ' имеет 6 ходов')

            if (( 1 <= self.position_x < 2) or (size_x -1 <= self.position_x < size_x )) and (size_y -1 <= self.position_y < size_y -1):
                print('в этой клетке ' + self.name + ' имеет 6 ходов')

            if (( 1 <= self.position_x < 2) or (size_x -1 <= self.position_x < size_x )) and (size_y <= self.position_y):
                print('в этой клетке ' + self.name + ' имеет 4 хода')

            #
            if ((self.position_x < 1) or (size_x -1 < self.position_x)) and (size_y -2 <= self.position_y < size_y -1):
                print('в этой клетке ' + self.name + ' имеет 7 ходов')

            if ((self.position_x < 1) or (size_x -1 < self.position_x)) and (size_y -1 <= self.position_y < size_y -1):
                print('в этой клетке ' + self.name + ' имеет 4 хода')

            if ((self.position_x < 1) or (size_x -1 < self.position_x)) and (size_y <= self.position_y):
                print('в этой клетке ' + self.name + ' имеет 3 хода')

        if (self.position_y <= (size_y//2)):    # нижняя половина (4 по прямой)
            if(self.position_x >= 4) or (self.position_x <= size_x -4) and (self.position_y >=4):
                print('в этой клетке ' + self.name + ' имеет 16 ходов')

            if (4 > self.position_x >= 3) or (size_x -3 <= self.position_x < size_x - 4):
                if (1 > self.position_y >= 0):
                    print('в этой клетке ' + self.name + ' имеет 11 ходов')
                if (2 > self.position_y >= 1):
                    print('в этой клетке ' + self.name + ' имеет 12 ходов')
                if (3 > self.position_y >= 2):
                    print('в этой клетке ' + self.name + ' имеет 13 ходов')
                if (4 > self.position_y >= 3):
                    print('в этой клетке ' + self.name + ' имеет 14 ходов')
                if (self.position_y >=4):
                    print('в этой клетке ' + self.name + ' имеет 15 ходов')

            if (3 > self.position_x >= 2) or (size_x -2 <= self.position_x < size_x - 3):
                if (1 > self.position_y >= 0):
                    print('в этой клетке ' + self.name + ' имеет 10 ходов')
                if (2 > self.position_y >= 1):
                    print('в этой клетке ' + self.name + ' имеет 11 ходов')
                if (3 > self.position_y >= 2):
                    print('в этой клетке ' + self.name + ' имеет 12 ходов')
                if (4 > self.position_y >= 3):
                    print('в этой клетке ' + self.name + ' имеет 13 ходов')
                if (self.position_y >=4):
                    print('в этой клетке ' + self.name + ' имеет 14 ходов')

            if (2 > self.position_x >= 1) or (size_x -1 <= self.position_x < size_x):
                if (1 > self.position_y >= 0):
                    print('в этой клетке ' + self.name + ' имеет 9 ходов')
                if (2 > self.position_y >= 1):
                    print('в этой клетке ' + self.name + ' имеет 10 ходов')
                if (3 > self.position_y >= 2):
                    print('в этой клетке ' + self.name + ' имеет 11 ходов')
                if (4 > self.position_y >= 3):
                    print('в этой клетке ' + self.name + ' имеет 12 ходов')
                if (self.position_y >=4):
                    print('в этой клетке ' + self.name + ' имеет 13 ходов')

            if (1 > self.position_x >= 0) or (size_x <= self.position_x):
                if (1 > self.position_y >= 0):
                    print('в этой клетке ' + self.name + ' имеет 8 ходов')
                if (2 > self.position_y >= 1):
                    print('в этой клетке ' + self.name + ' имеет 9 ходов')
                if (3 > self.position_y >= 2):
                    print('в этой клетке ' + self.name + ' имеет 10 ходов')
                if (4 > self.position_y >= 3):
                    print('в этой клетке ' + self.name + ' имеет 11 ходов')
                if (self.position_y >=4):
                    print('в этой клетке ' + self.name + ' имеет 12 ходов')
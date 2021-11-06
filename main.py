from ChessPieceArbitrary1 import ChessPieceArbitrary
from ChessPieceHorse import ChessPieceHorse
from ChessPiece import ChessPiece

Arbitrary = ChessPieceArbitrary
Arbitrary.position_x = int(input('Введите координаты фигуры X:'))
Arbitrary.position_y = (int(input('Введите координаты фигуры Y:')))
Arbitrary.size_x = (int(input('Введите длинну шахматного поля:')))
Arbitrary.size_y = (int(input('Введите высоту шахматного поля:')))
print (Arbitrary.number_of_possible_moves)

Arbitrary.position_x = int(input('Введите координаты фигуры X:'))
Arbitrary.position_y = (int(input('Введите координаты фигуры Y:')))
while True:
    if(Arbitrary.position_x! = "") and (Arbitrary.position_y! = ""):

Horse = ChessPieceHorse(int(input('Введите координаты фигуры X:')), int(input('Введите координаты фигуры Y:')))
print(Horse.number_of_possible_moves(int(input('Введите длинну шахматного поля:')), int(input('Введите высоту шахматного поля:'))))
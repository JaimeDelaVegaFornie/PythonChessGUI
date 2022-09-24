import os

import Board

b = Board.Board()

b.printTable()
    
End = False;#TODO-> Cambiar esto por atributo propio de la clase board (Algo estilo board.End que compruebe si hay jaque mate o no)

while not End:

    move = input()

    print("\n"*20)

    b.move(move)
    b.printTable()

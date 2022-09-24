import os
import Board


b = Board.Board()

#TODO-> Cambiar esto por atributo propio de la clase board (Algo estilo board.End que compruebe si hay jaque mate o no)
End = False;

while not End:
    b.print_board()
    move = input()
    End = b.move(move)
    print("\n"*2)

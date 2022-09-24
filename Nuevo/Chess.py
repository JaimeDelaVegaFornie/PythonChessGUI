import os

import Board

b = Board.Board()

b.printTable()
move = input()

print("\n"*20)

b.move(move)
b.printTable()
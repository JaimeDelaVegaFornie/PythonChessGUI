import os
import Board

def game():
    b = Board.Board()

    End = False;



    while not End:
        b.print_board()
        move = input()
        End = b.move(move)
        print("\n"*2)






f = open("version.txt", "r")
ver = f.readline()
f.close()

f = open("tutorial_short.txt")
tutorial = f.read()
f.close()


print('Welcome to Chess in Python version ',ver)
print(tutorial)
print('If you want to know more, see our long manual pressing t, if you want to play, press any other key')
opt = input()
if opt=="t":
    pass ## TODO: If user asks for manual open a file with full explanation, credits and chess tutorial
print('\n'*50   )
game()

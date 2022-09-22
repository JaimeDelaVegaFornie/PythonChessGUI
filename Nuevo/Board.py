import Pieces

class Board():

    def __init__(self):
        self.board=[]
        for i in range(8):
            self.board.append([None]*8)

        #Piezas blancas
        self.board[7][0] = piece.Rook(True)
        self.board[7][1] = piece.Knight(True)
        self.board[7][2] = piece.Bishop(True)
        self.board[7][3] = piece.Queen(True)
        self.board[7][4] = piece.King(True)
        self.board[7][5] = piece.Bishop(True)
        self.board[7][6] = piece.Knight(True)
        self.board[7][7] = piece.Rook(True)

        for i in range(8):
            self.board[7][i]=piece.Pawn(True)


        #Piezas negras
        for i in range(8):
            self.board[0][i]=piece.Pawn(False)

        self.board[7][0] = piece.Rook(False)
        self.board[7][1] = piece.Knight(False)
        self.board[7][2] = piece.Bishop(False)
        self.board[7][3] = piece.Queen(False)
        self.board[7][4] = piece.King(False)
        self.board[7][5] = piece.Bishop(False)
        self.board[7][6] = piece.Knight(False)
        self.board[7][7] = piece.Rook(False)


    def print_board(self):
        pass

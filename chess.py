class Chess():
    def __init__(self):
        self.board = Board()
        self.hertz = 60
class Board():
    def __init__(self):
        self.board = [['R','N','B','K','Q','B','N','R'],
                      ['P','P','P','P','P','P','P','P'],
                      [' ',' ',' ',' ',' ',' ',' ',' '],
                      [' ',' ',' ',' ',' ',' ',' ',' '],
                      [' ',' ',' ',' ',' ',' ',' ',' '],
                      [' ',' ',' ',' ',' ',' ',' ',' '],
                      ['P','P','P','P','P','P','P','P'],
                      ['R','N','B','K','Q','B','N','R']]
        self.length = 8
        self.transl_piece = {'P' : Pawn, 'N' : Knight, 'B' : Bishop, 'K' : Knight, 'Q' : Queen}
        self.pieces = []
        
        count = 0
        isWhite = True
        for x, y in range(self.length, self.length):
            if(count == 16):
                isWhite = False
            aux = self.board[x][y]
            if(aux in self.transl_piece.keys()):
                self.pieces.append(self.transl_piece.get(aux)(x, y, isWhite))
                count+=1
            
    def print_board(self):
        print(self.board, sep = '\n')
    def refresh():
        pass


class Piece():
    def __init__(self, x, y, isWhite):
        self.x = x
        self.y = y
        self.isWhite = isWhite

    def is_white(self):
        pass

class Knight(Piece):
    def __init__(self):
        pass

class Pawn(Piece):
    def __init__(self):
        pass
    
class Bishop(Piece):
    def __init__(self):
        pass

class Rook(Piece):
    def __init__(self):
        pass


class Queen(Piece):
    def __init__(self):
        pass


class King(Piece):
    def __init__(self):
        pass

class Piece:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def is_white(self):
        return self.color == 'W'

    def is_black(self):
        return self.color == 'B'

    def __str__(self):
        if self.is_black():
            return self.name.lower()
        elif self.is_white():
            return self.name
        else:
            return ' '

class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'P'

    def is_valid_move(self):
        pass

class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'R'

    def is_valid_move(self):
        pass

class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'N'
        # moves = ["x+j,y+2i", "x+2j,y+i"]

    def is_valid_move(self):
        pass

class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'B'

    def is_valid_move(self):
        pass

class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'Q'

    def is_valid_move(self,board,sx,sy,dx,dy):
        if board.piece(x,y).color==board.side:
            if sx==dx or sy==dy:
                pass
        else False



class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'K'

    def is_valid_move(self,board,sx,sy,dx,dy):
        pass

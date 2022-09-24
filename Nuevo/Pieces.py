class Piece:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def isWhite(self):
        return self.color == 'W'

    def isBlack(self):
        return self.color == 'B'

class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'P'

class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'R'

class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'N'
        # moves = ["x+j,y+2i", "x+2j,y+i"]

class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'B'

class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'Q'

class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'K'
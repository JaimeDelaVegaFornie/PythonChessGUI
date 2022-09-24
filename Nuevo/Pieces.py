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
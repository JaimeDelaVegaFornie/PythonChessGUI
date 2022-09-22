class Piece():

    def __init__(self,color):
        self.color = color
        self.name = ""

    def is_valid_move(self):
        pass

    def is_white(self):
        return self.color

    def __str__(self):
        return self.name

class Knight(Piece):

    def __init__(self,Bool):
        super().__init__(color)
        self.name = "N"

    def is_valid_move(self,board,start,to):
        pass


class Pawn(Piece):

    def __init__(self):
        super().__init__(color)
        self.name = "P"

    def is_valid_move(self):
        pass

class Bishop(Piece):

    def __init__(self):
        super().__init__(color)
        self.name = "B"

    def is_valid_move(self):
        pass

class Rook(Piece):

    def __init__(self):
        super().__init__(color)
        self.name = "R"

    def is_valid_move():
        pass

class Queen(Piece):

    def __init__(self):
        super().__init__(color)
        self.name = "Q"

    def is_valid_move(self):
        pass

class King(Piece):

    def __init__(self):
        super().__init__(color)
        self.name = "K"

    def is_valid_move(self):
        pass

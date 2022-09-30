import itertools

import Pieces


class Board:
    """ A class used for initializing the chess board and manage it.

        Attributes:
        ----------
        table : matrix
        turn : int
        side : True (White), False (black)
        piece_dict : A dictionary with all pieces

        Methods
        ----------
        coord_to_pos(int : x, int : y)
            translates chess board coordinates to language positions
        pos_to_coord(int : x, int : y)
            translates language positions to board coordinates
        read_FEN(str : FEN)
            reads and translates FEN string containing all positions into the chess table
        write_FEN()
            opens log.txt file and writes the current positions translated into FEN string
        parse_move(str : move)
            prints moves translated into table positions (debugging purposes or backend purposes)
        move(str : moveStr)
            moves piece into the next square in 'pSq1Sq2' format (p : piece, Sq1 : 1st position:
                                                                  Sq2 : last position)
            Needs some changes like when a piece promotes.
        print_board()
            prints the current state of chess' board, displaying (1-8), (a-h) notation
        """

    PAWN, ROOK, KNIGHT, BISHOP, QUEEN, KING = 'P', 'R', 'N', 'B', 'Q', 'K'
    turn = 0
    side = True


    def __init__(self, FEN=None):
        self.piece_dict = {
            Board.PAWN: Pieces.Pawn,
            Board.ROOK: Pieces.Rook,
            Board.KNIGHT: Pieces.Knight,
            Board.BISHOP: Pieces.Bishop,
            Board.QUEEN: Pieces.Queen,
            Board.KING: Pieces.King
        }
        self.table = [[None for x in range(8)] for y in range(8)]
        self.turn = 0
        self.side = True
        self.read_FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR" if FEN is None else FEN)
        self.log = open("log.txt", "w")

    def __del__(self):
        self.log.write("\n" + self.write_FEN())
        self.log.close()

    def coord_to_pos(x, y):
        """ int : x,y : coordinates """
        return chr(ord('a') + x), chr(ord('1') + y)

    def pos_to_coord(file, rank):
        """ char : x,y : positions """
        return (ord(file) - ord('a'), ord(rank) - ord('1'))

    def read_FEN(self, FEN):
        """ str : FEN : tables' state """
        def FEN_white(c):
            """ char : c : checks if piece is white """
            return c in "PRNBQK"
        def FEN_black(c):
            """ char : c : checks if piece is black"""
            return c in "prnbqk"
        def assign_piece(x, y, c):
            """ int : x, y: coordinates
                char c : color
                Initializes the piece in table
            """
            color = ('W' if FEN_white(c) else 'B')
            c = c.upper()
            return self.piece_dict[c](x,y,color)

        accepted = "prnbqkPRNBQK/bw0123456789"
        if any(c not in accepted for c in FEN):
            self.read_FEN("8/8/8/8/8/8/8/8")
            return
        FEN = FEN.replace(" ", "");
        rows = FEN.split('/')[::-1]
        for y in range(len(rows)):
            for x in range(len(rows[y])):
                c = rows[y][x]
                if c.isdigit():
                    for _ in itertools.repeat(None, int(c)):
                        self.table[y][x] = None
                        x += 1
                    continue
                self.table[y][x] = assign_piece(x, y, c)

    def write_FEN(self):
        table = self.table[::-1]
        FEN = ""
        for y in range(len(table)):
            count = 0
            for x in range(len(table[y])):
                square = table[y][x]
                if square is None:
                    count += 1
                else:
                    FEN += (str(count) if count != 0 else "") + (str(square) if square.is_white() else str(square).lower())
                    count = 0
            FEN += (str(count) if count != 0 else "") + ("/" if y < 7 else "")
        return FEN

    def parse_move(self, move): #debug, backend function
        """ str : move """
        def parse_pos(pos):
            """ str : pos
                prints the positions' swap
            """
            print(pos[0] + "x" + pos[1] + " --> ", end="")
            x, y = ord(pos[0]) - ord('a'), ord(pos[1]) - ord('1')
            print(str(x) + "x" + str(y))
            return x, y

        piece = Board.PAWN # debugging purposes
        if move[0].upper() in self.piece_dict.keys():
            piece = move[0]
            move = move[1:]
        sx, sy = parse_pos(move[:2])
        dx, dy = parse_pos(move[-2:])
        return piece, sx, sy, dx, dy



    def piece(self,x,y):
        """
        Should return the piece (as an object) that is in the (x,y) position in the board
        """
        pass



    def move(self, moveStr): ## TODO: make sure that sx, sy, dx, dy are inside the board
        """ str : moveSTr """
        def log_move(piece, sx, sy, dx, dy):
            """ char : piece, sx, sy, dx, dy
                writes current move into log.txt
            """
            if self.side:
                self.log.write(str(self.turn + 1) + ".")
            self.log.write(" ")
            if piece is not Board.PAWN:
                self.log.write(piece if self.turn > 0 else piece.lower())
            self.log.write(sx + sy + dx + dy)
            if not self.side:
                self.log.write("\n")

        if moveStr == "end":
            return True
        piece, sx, sy, dx, dy = self.parse_move(moveStr)
        self.table[dy][dx] = self.table[sy][sx]
        self.table[sy][sx] = None
        sx, sy = Board.coord_to_pos(sx, sy)
        dx, dy = Board.coord_to_pos(dx, dy)
        log_move(piece, sx, sy, dx, dy)
        self.turn += 1 if not self.side else 0
        self.side = not self.side
        return False

    def print_board(self):
        print("\n".join(
            "".join(["{}".format((' ' + chr(ord('8')-i) if j == 0 else '') + ('-' if piece is None else str(piece)).center(3)) for j, piece in enumerate(row)]) for i, row in
            enumerate(self.table[::-1])))
        print(("  ") + "\n".join(["".join("{}".format(chr(ord('A')+i)).center(3) for i in range(len(self.table)))]))

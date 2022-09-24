import itertools

import Pieces


class Board:
    PAWN, ROOK, KNIGHT, BISHOP, QUEEN, KING = 'P', 'R', 'N', 'B', 'Q', 'K'
    table = [[]]
    turn = 0
    side = 1  # 1 = white, -1 = black

    def __init__(self, FEN=None):
        self.table = [[None for x in range(8)] for y in range(8)]
        self.turn = 0
        self.side = 1
        self.read_FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR" if FEN is None else FEN)
        self.log = open("log.txt", "w")

    def __del__(self):
        self.log.write("\n" + self.write_FEN())
        self.log.close()

    def coord_to_pos(x, y):
        return chr(ord('a') + x), chr(ord('1') + y)

    def pos_to_coord(file, rank):
        return ord(file) - ord('a'), ord(rank) - ord('1')

    def read_FEN(self, FEN):
        def FEN_white(c):
            return c in "PRNBQK"
        def FEN_black(c):
            return c in "prnbqk"
        def assign_piece(x, y, c):
            color = ('W' if FEN_white(c) else 'B')
            c = c.upper()
            piece_dict = {
                Board.PAWN: Pieces.Pawn(x, y, color),
                Board.ROOK: Pieces.Rook(x, y, color),
                Board.KNIGHT: Pieces.Knight(x, y, color),
                Board.BISHOP: Pieces.Bishop(x, y, color),
                Board.QUEEN: Pieces.Queen(x, y, color),
                Board.KING: Pieces.King(x, y, color)
            }
            return piece_dict[c]

        accepted = "prnbqkPRNBQK/bw0123456789 "
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
                c = table[y][x]
                if c is None:
                    count += 1
                else:
                    FEN += (str(count) if count != 0 else "") + (c.name if c.is_white() else c.name.lower())
                    count = 0
            FEN += (str(count) if count != 0 else "") + ("/" if y < 7 else "")
        return FEN

    def parse_move(self, m):
        def parse_pos(pos):
            print(pos[0] + "x" + pos[1] + " --> ", end="")
            x, y = ord(pos[0]) - ord('a'), ord(pos[1]) - ord('1')
            print(str(x) + "x" + str(y))
            return x, y

        piece = Board.PAWN
        if m[0].upper() in [Board.ROOK, Board.KNIGHT, Board.BISHOP, Board.QUEEN, Board.KING]:
            piece = m[0]
            m = m[1:]
        sx, sy = parse_pos(m[:2])
        dx, dy = parse_pos(m[-2:])
        return piece, sx, sy, dx, dy

    def move(self, moveStr):
        def log_move(piece, sx, sy, dx, dy):
            if self.side > 0:
                self.log.write(str(self.turn + 1) + ".")
            self.log.write(" ")
            if piece is not Board.PAWN:
                self.log.write(piece if self.turn > 0 else piece.lower())
            self.log.write(sx + sy + dx + dy)
            if self.side < 0:
                self.log.write("\n")

        if moveStr == "end":
            return True
        piece, sx, sy, dx, dy = self.parse_move(moveStr)
        self.table[dy][dx] = self.table[sy][sx]
        self.table[sy][sx] = None
        sx, sy = Board.coord_to_pos(sx, sy)
        dx, dy = Board.coord_to_pos(dx, dy)
        log_move(piece, sx, sy, dx, dy)
        self.turn += 1 if self.side < 0 else 0
        self.side *= -1
        return False

    def print_board(self):
        print("\n".join(
            "".join(["{}".format('-' if piece is None else str(piece)).center(3) for piece in row]) for row in
            self.table[::-1]))

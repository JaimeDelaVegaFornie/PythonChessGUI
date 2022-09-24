import Pieces

class Board:
    PAWN, ROOK, KNIGHT, BISHOP, QUEEN, KING = 'P', 'R', 'N', 'B', 'Q', 'K'
    table = [[]]
    turn = 0
    side = 1

    def __init__(self, FEN = None):
        self.table = [[None for x in range(8)] for y in range(8)]
        self.turn = 0
        self.side = 1  # 1 = white, -1 = black
        if FEN is None:
            FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        self.readFEN(FEN)

    def readFEN(self, FEN):
        def FENWhite(p):
            return p in "PRNBQK"
        def FENBlack(p):
            return p in "prnbqk"
        def assignPiece(x, y, color, p):
            if p == Board.PAWN:
                return Pieces.Pawn(x, y, color)
            elif p == Board.ROOK:
                return Pieces.Rook(x, y, color)
            elif p == Board.KNIGHT:
                return Pieces.Knight(x, y, color)
            elif p == Board.BISHOP:
                return Pieces.Bishop(x, y, color)
            elif p == Board.QUEEN:
                return Pieces.Queen(x, y, color)
            elif p == Board.KING:
                return Pieces.King(x, y, color)

        FEN = FEN.replace(" ", "");
        rows = FEN.split('/')
        y = 7
        for i in range(8):
            x = 0
            for j in range(len(rows[i])):
                if FENWhite(rows[i][j]):
                    self.table[y][x] = assignPiece(x, y, 'W', rows[i][j])
                    x += 1
                elif FENBlack((rows[i][j])):
                    self.table[y][x] = assignPiece(x, y, 'B', rows[i][j].upper())
                    x += 1
                else:
                    for j in range(ord(rows[i][j]) - ord('0')):
                        self.table[y][x] = None
                        x += 1
            y -= 1

    def writeFEN(self):
        FEN = ""
        for y in range(7, -1, -1):
            count = 0
            for x in range(8):
                if self.table[y][x] is None:
                    count += 1
                elif self.table[y][x].name in [Board.PAWN, Board.ROOK, Board.KNIGHT, Board.BISHOP, Board.QUEEN, Board.KING]:
                    if count != 0:
                        FEN += str(count)
                        count = 0
                    if self.table[y][x].isBlack():
                        FEN += self.table[y][x].name.lower()
                    elif self.table[y][x].isWhite():
                        FEN += self.table[y][x].name
                    x += 1
            if count != 0:
                FEN += str(count)
            if y > 0:
                FEN += '/'
        return FEN

    def findInRow(self, piece, row):
        for i in range(0,8):
            if self.table[row][i].name == piece:
                return i
        return -1

    # TODO: IF THERE ARE TWO PAWNS IN THE SAME COLUMN THAT EAT
    def findInCol(self, piece, col):
        for i in range(0,8):
            if self.table[i][col].name == piece:
                return i
        return -1

    def parseMove(self, m):
        def parsePos(pos):
            x, y = ord(pos[0]) - ord('a'), ord(pos[1]) - ord('1')
            return x, y

        piece = Board.PAWN
        sx = sy = dx = dy = i = promotion = None
        # gets piece
        if m[0] in [Board.ROOK, Board.KNIGHT, Board.BISHOP, Board.QUEEN, Board.KING]:
            piece = m[0]
            m = m[1:]
        # checks if it's a promotion
        if m[-1] in [Board.ROOK, Board.KNIGHT, Board.BISHOP, Board.QUEEN]:  # its a promotion
            promotion = m[-1]
            m = m[:-1]
        # gets destination position
        dx, dy = parsePos(m[-2:])
        m = m[:-2]
        # only case where there is no source position is when it's a pawn forward movement
        if not m:
            sx = dx
            sy = Board.findInCol(self, piece, sx)
        else:
            # sanitizes if its a capture
            if m[-1] == 'x':
                m = m[:-1]
            # gets source position
            if len(m) == 2:
                sx, sy = parsePos(m)
            elif ord(m[0]) in range(ord('a'), ord('i')):
                sx = ord(m[0]) - ord('a')
                sy = Board.findInCol(self, piece, sx)
            else:
                sy = ord(m[0]) - ord('0')
                sx = Board.findInRow(self, piece, sy)

        print(piece + " moves from %dx%d to %dx%d" % (sx, sy, dx, dy))
        return sx, sy, dx, dy

    def move(self, moveStr):
        sx, sy, dx, dy = self.parseMove(moveStr)
        self.table[dy][dx] = self.table[sy][sx]
        self.table[sy][sx] = None
        self.turn += 1
        self.side *= -1



    def printTable(self):
        for y in range(7, -1, -1):
            for x in range(8):
                if self.table[y][x] is None:
                    print("-", end=' ')
                else:
                    p = self.table[y][x].name
                    if self.table[y][x].color == 'B':
                        p = p.lower()
                    print(p, end=' ')
            print()
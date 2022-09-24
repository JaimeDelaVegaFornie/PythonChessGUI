	class move
		// positions of the piece (before move)
		x	->	x pos
		y	->	y pos
		// directions of the piece (to move) [1, -1]
		j	->	x dir
		i	->	y dir
		// number of times to repeat move (rook, bishop, queen)
		r	->	nº of reps
		// if it takes
		t	->	takes
		// if its the first move
		f	->	first move

examples in pieces

	torre:
		xjr | yir
	caballo:
		x+j, y+2i | x+2j, y+i
	alfil:
		xjr, yir
	reina:
		xjr | yir | xjr, yir
	rey:
		x+j | y+j | x+j, y+i
	peon:
		yi+f | y+tj

    def subCalc(e):
        r = 1
        for c in e:
            r *= locals()[e]
        return r

    def calc(e):
        r = 0
        P = [str(p) for p in e.split('+') if p.strip()]
        for p in P:
            r += Piece.subCalc(p)
        return r

    L = [str(e) for e in ec.split(',') if e.strip()]


    def findInRow(self, piece, row):
        for i in range(0,8):
            if self.table[row][i] is not None and self.table[row][i].name == piece:
                return i
        return -1

    # TODO: IF THERE ARE TWO PAWNS IN THE SAME COLUMN THAT EAT
    def findInCol(self, piece, col):
        for i in range(0,8):
            if self.table[i][col] is not None and self.table[i][col].name == piece:
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
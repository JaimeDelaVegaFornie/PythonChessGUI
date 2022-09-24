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
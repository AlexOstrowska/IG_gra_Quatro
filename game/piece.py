

class Piece:

    def __init__(self, id=1, round_shape=False, big_size=False, light_color=False, top_hole=False):
        self.round_shape = round_shape
        self.big_size = big_size
        self.light_color = light_color
        self.top_hole = top_hole
        self.id = id
        self.player = None

    def __str__(self):
        return 'pionek {} {} {} {}'.format(
            'okrągły' if self.round_shape else 'kwadratowy',
            'jasny' if self.light_color else 'ceimny',
            'z dziurą' if self.top_hole else 'bez dziury',
            'duży' if self.big_size else 'mały'
        )

    def __repr__(self):
        return 'piece: '+str(self.id)

pieces_list_definition = [
    Piece(1, False, False, False, False),
    Piece(2, True, False, False, False),
    Piece(3, False, True, False, False),
    Piece(4, True, True, False, False),
    Piece(5, False, False, True, False),
    Piece(6, True, False, True, False),
    Piece(7, False, True, True, False),
    Piece(8, True, True, True, False),
    Piece(9, False, False, False, True),
    Piece(10, True, False, False, True),
    Piece(11, False, True, False, True),
    Piece(12, True, True, False, True),
    Piece(13, False, False, True, True),
    Piece(14, True, False, True, True),
    Piece(15, False, True, True, True),
    Piece(16, True, True, True, True)
]

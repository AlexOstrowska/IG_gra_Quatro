def check_finish(board):
    for row in board:
        res = {
            'round_shape': True,
            'light_color': True,
            'top_hole': True,
            'big_size': True,
            'square_shape': True,
            'dark_color': True,
            'no_hole': True,
            'small_size': True,
        }
        for field in row:
            if field == None:
                for i in res:
                    res[i] = False

            if field:
                if field.round_shape:
                    res['square_shape'] = False
                else:
                    res['round_shape'] = False

                if field.light_color:
                    res['light_color'] = False
                else:
                    res['dark_color'] = False

                if field.top_hole:
                    res['top_hole'] = False
                else:
                    res['no_hole'] = False

                if field.big_size:
                    res['big_size'] = False
                else:
                    res['small_size'] = False
            else:
                break

        for f in res:
            if res[f]:
                return True


    r_board = list(zip(*board))[::-1]

    for row in r_board:
        res = {
            'round_shape': True,
            'light_color': True,
            'top_hole': True,
            'big_size': True,
            'square_shape': True,
            'dark_color': True,
            'no_hole': True,
            'small_size': True,
        }
        for field in row:
            if field == None:
                for i in res:
                    res[i] = False
            if field:
                if field.round_shape:
                    res['square_shape'] = False
                else:
                    res['round_shape'] = False

                if field.light_color:
                    res['light_color'] = False
                else:
                    res['dark_color'] = False

                if field.top_hole:
                    res['top_hole'] = False
                else:
                    res['no_hole'] = False

                if field.big_size:
                    res['big_size'] = False
                else:
                    res['small_size'] = False
            else:
                break

        for f in res:
            if res[f]:
                return True

    d_board = list([board[0][0], board[1][1], board[2][2], board[3][3]])
    res = {
        'round_shape': True,
        'light_color': True,
        'top_hole': True,
        'big_size': True,
        'square_shape': True,
        'dark_color': True,
        'no_hole': True,
        'small_size': True,
    }
    for field in d_board:
        if field == None:
            for i in res:
                res[i] = False

        if field:
            if field.round_shape:
                res['square_shape'] = False
            else:
                res['round_shape'] = False

            if field.light_color:
                res['light_color'] = False
            else:
                res['dark_color'] = False

            if field.top_hole:
                res['top_hole'] = False
            else:
                res['no_hole'] = False

            if field.big_size:
                res['big_size'] = False
            else:
                res['small_size'] = False
        else:
            break
    for f in res:
        if res[f]:
            return True
    d2_board = list([board[3][0], board[2][1], board[1][2], board[0][3]])
    res = {
        'round_shape': True,
        'light_color': True,
        'top_hole': True,
        'big_size': True,
        'square_shape': True,
        'dark_color': True,
        'no_hole': True,
        'small_size': True,
    }
    for field in d2_board:
        if field == None:
            for i in res:
                res[i] = False

        if field:
            if field.round_shape:
                res['square_shape'] = False
            else:
                res['round_shape'] = False

            if field.light_color:
                res['light_color'] = False
            else:
                res['dark_color'] = False

            if field.top_hole:
                res['top_hole'] = False
            else:
                res['no_hole'] = False

            if field.big_size:
                res['big_size'] = False
            else:
                res['small_size'] = False
        else:
            break
    for f in res:
        if res[f]:
            return True
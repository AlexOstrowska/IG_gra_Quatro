from flask import Flask, render_template, request, flash, redirect
from game.piece import pieces_list_definition
from copy import deepcopy
from game.finish import check_finish
from random import choice

app = Flask(__name__)
app.secret_key = 'kluczyk'

backup = deepcopy(pieces_list_definition)

board = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
]
turn = 0
global_piece = None
player = None
pps = deepcopy(backup)


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/game', methods=['POST', 'GET'])
def game():
    global global_piece
    global turn
    global board
    global player
    global pps
    global backup

    if request.method == 'POST':
        field_to_insert_id = request.form.get('field')
        piece_id = int(request.form.get('piece'))

        board[int(field_to_insert_id[1])][int(field_to_insert_id[0])] = global_piece

        turn += 1
        global_piece = [p for p in pps if p.id == piece_id][0]
        pps.remove(global_piece)
        #print(backup, len(backup))
        #print(pps, len(pps))
        if check_finish(board):
            flash('wygrał ' + player, 'success')
            return redirect('/')
        if not pps:
            flash('remis')
            return redirect('/')

    free_field = []
    for i, row in enumerate(board):
        for j, field in enumerate(row):
            if not field:
                free_field.append('{}{}'.format(j, i))

    if not turn:
        piece = choice(pps)
        global_piece = piece
        pps.remove(piece)

    if turn == 0 or turn % 2 == 0:
        player = 'gracz 1'
    else:
        player = 'gracz 2'

    return render_template('game.html', pieces=pps, board=board, free_fields=free_field,
                           piece=global_piece, player=player)


@app.route('/rules')
def zasady():
    return render_template('rules.html')


@app.route('/reset')
def reset():
    global global_piece
    global turn
    global board
    global player
    global pps
    global backup
    board = [
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
    ]
    turn = 0
    global_piece = None
    player = None
    x = deepcopy(backup)
    #print(x, len(x))
    pps = None
    pps = x
    return redirect('/game')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, flash, redirect
from game.piece import pieces_list_definition
from game.finish import check_finish
from random import choice

app = Flask(__name__)
app.secret_key = 'kluczyk'

board = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
]
turn = 0
global_piece = None
player = None


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

    if request.method == 'POST':
        field_to_insert_id = request.form.get('field')
        piece_id = int(request.form.get('piece'))

        board[int(field_to_insert_id[1])][int(field_to_insert_id[0])] = global_piece

        turn += 1
        global_piece = [p for p in pieces_list_definition if p.id == piece_id][0]
        pieces_list_definition.remove(global_piece)
        #if check_finish(board):
        #    flash('wygrał '+ player, 'success')
        #    return redirect('/')

    free_field = []
    for i, row in enumerate(board):
        for j, field in enumerate(row):
            if not field:
                free_field.append('{}{}'.format(j, i))

    if not turn:
        piece = choice(pieces_list_definition)
        global_piece = piece
        pieces_list_definition.remove(piece)

    if turn == 0 or turn % 2 == 0:
        player = 'gracz 1'
    else:
        player = 'gracz 2'

    return render_template('game.html', pieces=pieces_list_definition, board=board, free_fields=free_field,
                           piece=global_piece, player=player)


@app.route('/rules')
def zasady():
    return render_template('rules.html')


@app.route('/reset')
def reset():
    game()
    return redirect('/game')


if __name__ == '__main__':
    app.run(debug=True)

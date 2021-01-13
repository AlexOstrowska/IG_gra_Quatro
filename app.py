from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/rules')
def zasady():
    return render_template('rules.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('checkerboard.html', row=8, col=8, color_one='purple', color_two='yellow')

@app.route('/<int:x>')
def var_row(x):
    return render_template('checkerboard.html', row=x, col=8, color_one='purple', color_two='yellow')

@app.route('/<int:x>/<int:y>')
def var_rowscols(x,y):
    return render_template('checkerboard.html', row=x, col=y, color_one='grey', color_two='green')





if __name__ == ("__main__"):
    app.run(debug=True)
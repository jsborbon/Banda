from flask import Flask, render_template
from Logic.Band import Band

app = Flask(__name__)


@app.route('/banda')
def index():
    b = Band()
    # return render_template('index.html', b.assignBand())
    return render_template('index.htm', assignedBand=b.assignBand(), tuneBand=b.tuneBand())


@app.route('/')
def prueba():
    return render_template('prueba.htm')


if __name__ == "__main__":
    app.run(debug=True)

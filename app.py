from flask import Flask, render_template
from logic.Band import Band

app = Flask(__name__)


@app.route('/Mariachi')
def index():
    b = Band()
    # return render_template('Mariachi.html', b.assignBand())
    return render_template('Mariachi.htm', assignedBand=b.assignBand(), tuneBand=b.tuneBand(), playBand=b.playBand())


@app.route('/')
def prueba():
    # return render_template('Index.htm')
    return render_template('Index.htm')


if __name__ == "__main__":
    app.run(debug=True)

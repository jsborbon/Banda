from flask import Flask, render_template, session
from logic.Band import Band


app = Flask(__name__)
app.secret_key = 'This-is-a-real-secret-key'
b = Band()
tuneBand = b.tuneBand()
playBand = b.playBand()


@app.route('/Mariachi')
def index():
    assignedBandL = session['Band']
    tuneBandL = tuneBand
    return render_template('Mariachi.htm', assignedBand=assignedBandL, tuneBand=tuneBandL)


@app.route('/')
def prueba():
    session['Band'] = b.assignBand()
    return render_template('Index.htm')


@app.route('/Play')
def play():
    assignedBandL = session['Band']
    playBandL = playBand
    return render_template('playBand.htm', assignedBand=assignedBandL, playBand=playBandL)


if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, render_template, session
from logic.Band import Band


app = Flask(__name__)
app.secret_key = 'This-is-a-real-secret-key'
b = Band()
tuneBand = b.tuneBand()
playBand = b.playBand()


@app.route('/Mariachi')
def index():
    assignedBandL = session['Band']
    tuneBandL = tuneBand
    return render_template('Mariachi.htm', assignedBand=assignedBandL, tuneBand=tuneBandL)


@app.route('/')
def prueba():
    session['Band'] = b.assignBand()
    return render_template('Index.htm')


@app.route('/Play')
def play():
    assignedBandL = session['Band']
    playBandL = playBand
    return render_template('playBand.htm', assignedBand=assignedBandL, playBand=playBandL)


if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 1dce1361caed8500093f8aac1a98a176b319de1b

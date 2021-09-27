from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "inuyasha"

@app.route('/', methods=['GET'])
def showForm():
    return render_template('index.html')


@app.route('/processingInformation', methods=['POST'])
def getInformation():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')

@app.route('/results', methods=['GET'])
def showInformation():
    return render_template('results.html')

if __name__ == "__main__":
    app.run( debug = True )
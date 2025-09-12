from flask import Flask, render_template, url_for, request, redirect, jsonify 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz1', methods=('POST','GET'))
def quiz1():
    if request.method == 'POST':
        correct_answers = ['Nicht-Regierungsorganisationen (NGOs)', 'Politische Stiftungen', 'temporäre Projekt-Teams']
        answers = request.form.getlist("answers")
        correctly_chosen = [i for i in answers if i in correct_answers]
        if "Firmen" in answers or "Einzelpersonen" in answers or "Ausländische Regierungen" in answers:
            return redirect(url_for('quizfail'))
        elif len(correctly_chosen) == 3:
            return redirect(url_for('quizsuccess'))
    return render_template('quiz1.html')

@app.route('/quiz2', methods=('POST','GET'))
def quiz2():
    if request.method == 'POST':
        correct_answers = ['erhebliches Bundesinteresse', 'Zweck nicht ohne Zuwendung']
        answers = request.form.getlist("answers")
        correctly_chosen = [i for i in answers if i in correct_answers]
        if "Firmen" in answers or "Einzelpersonen" in answers or "Ausländische Regierungen" in answers:
            return redirect(url_for('quizfail'))
        elif len(correctly_chosen) == 2 and len(answers) == 2:
            return redirect(url_for('quizsuccess'))
        else:
            return redirect(url_for('quizfail'))
    return render_template('quiz2.html')

@app.route('/quizfail')
def quizfail():
    return render_template('quizfail.html')

@app.route('/quizsuccess')
def quizsuccess():
    return render_template('quizsuccess.html')

if __name__ == '__main__':
    app.run(debug=True)
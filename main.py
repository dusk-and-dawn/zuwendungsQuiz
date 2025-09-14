from flask import Flask, render_template, url_for, request, redirect, session
import uuid
from db import add_to_main_db, show_db, get_db_connection, get_q, create_answer_table

app = Flask(__name__)
app.secret_key = "terrible_key_really_who_could_have_made_even_this"

db = get_db_connection('main.db')

create_answer_table(db)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz1', methods=('POST','GET'))
def quiz1():
    db = get_db_connection('main.db')
    session['id'] = str(uuid.uuid4())
    
    add_to_main_db(db=db, session=session['id'], score=0, q_answered=1)
    prev_q = 1
    # show_db(db)
    if request.method == 'POST':
        correct_answers = ['Nicht-Regierungsorganisationen (NGOs)', 'Politische Stiftungen', 'temporäre Projekt-Teams']
        answers = request.form.getlist("answers")
        correctly_chosen = [i for i in answers if i in correct_answers]
        
        if "Firmen" in answers or "Einzelpersonen" in answers or "Ausländische Regierungen" in answers or len(answers) == 0:
            return redirect(url_for('quizfail', prev_q=prev_q))
        elif len(correctly_chosen) == 3:
            return redirect(url_for('quizsuccess', prev_q=prev_q))
        elif len(correctly_chosen) != 3:
            return redirect(url_for('quizfail', prev_q=prev_q))
    return render_template('quiz1.html')

@app.route('/quiz2', methods=('POST','GET'))
def quiz2():
    if request.method == 'POST':
        correct_answers = ['erhebliches Bundesinteresse', 'Zweck nicht ohne Zuwendung']
        answers = request.form.getlist("answers")
        correctly_chosen = [i for i in answers if i in correct_answers]
        prev_q = 2
        if "Firmen" in answers or "Einzelpersonen" in answers or "Ausländische Regierungen" in answers:
            return redirect(url_for('quizfail'))
        elif len(correctly_chosen) == 2 and len(answers) == 2:
            return redirect(url_for('quizsuccess', prev_q=prev_q))
        else:
            return redirect(url_for('quizfail', prev_q=prev_q))
    return render_template('quiz2.html')

@app.route('/quizfail')
def quizfail():
    db = get_db_connection('main.db')
    print(f' at quiz fail : sessionid = {session['id']} type= {type(session['id'])}')
    prev_q = get_q(db, id=session['id'])
    print(f'prev_q: {prev_q}')
    return render_template('quizfail.html', prev_q=prev_q)

@app.route('/quizsuccess')
def quizsuccess():
    prev_q = 0
    return render_template('quizsuccess.html', prev_q=prev_q)

if __name__ == '__main__':
    app.run(debug=True)
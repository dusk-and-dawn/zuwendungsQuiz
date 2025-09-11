from flask import Flask, render_template, url_for, request, redirect, jsonify 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz1.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    resposta = render_template('index.html')
    return resposta
@app.route('/exemplo1')
def exemplo1():
    pessoa = {"nome":"Vinicius", "matricula":2200420}
    return render_template('exemplo1.html', dados=pessoa)
@app.route('/exemplo2')
def exemplo2():
    return render_template('exemplo2.html', nome='Vinicius', matricula=2200420, nota=5.1)
@app.route('/alunos')
def listagem_alunos():
    alunos = ['Ana Maria', 'Beatriz Silva', 'Carlos Eduardo', 'Daniel Santos', 'Emilia Ferreira']
    return render_template('alunos.html', disc='Desenvolvimento Web', lista_alunos=alunos)
app.run(debug=True)
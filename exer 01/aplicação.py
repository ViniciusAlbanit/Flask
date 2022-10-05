from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Olá mundo!"

@app.route('/ads')
def ads():
    s = "<h1>Bem-vindo á pagina do curso de ADS</h1>"
    s += "<p>Parágrafo com informação do curso de ADS</p>"
    return s

@app.route('/ads/2022')
def adas_2022():
    return "Página da turma de ADS de 2022"

@app.route('/disciplina/<nome>') # <nome> é um slug
def disciplina(nome):
    if nome == 'devweb':
        return "Essa é a página de disciplina de Desenvolvimento Web"
    elif nome == 'poo':
        return "Essa é página de disciplina de POO"
    else:
        return "Disciplina inexistente"

@app.route('/disciplina/<nome>/<int:ano>')
def disciplina_por_ano(nome, ano):
    return "O valor do nome é: {0}, e o valor do ano é: {1}".format(nome, ano)
app.run(debug=True, port=5005)

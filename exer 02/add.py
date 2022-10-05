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
app.run(debug=True)
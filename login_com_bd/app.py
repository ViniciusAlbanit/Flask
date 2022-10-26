from flask import Flask, render_template, request, session, redirect
from models.usuario import BancoDeDados

app = Flask(__name__)
app.secret_key = 'SENHA-MUITO-SECRETA'

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg_erro = ''
    if request.method == 'POST':
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        bd = BancoDeDados()
        if bd.existe_aluno(usuario, senha):
            session['usuario'] = usuario
            return redirect('/area_logada')
        else:
            msg_erro = 'Usuário e/ou senha incorretos!'
    return render_template('index.html', erro=msg_erro)

@app.route('/area_logada')
def area_logada():
    if 'usuario' in session:
        bd = BancoDeDados()
        dados_aluno = bd.obter_dados(session['usuario'])
        return render_template('area_logada.html', aluno=dados_aluno)
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
app.run(debug=True)
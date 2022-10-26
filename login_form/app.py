from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'SENHA-MUITO-SECRETA'

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg_erro = ''
    if request.method == 'POST':
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        if usuario == 'rafael' and senha == '1234':
            session['usuario'] = 'rafael'
            return redirect('/area_logada')
        elif usuario == 'maria' and senha == '1111':
            session['usuario'] = 'maria'
            return redirect('/area_logada')
        else:
            msg_erro = 'Usuário e/ou senha incorretos!'
    return render_template('index.html', erro=msg_erro)

@app.route('/area_logada')
def area_logada():
    if 'usuario' in session:
        nome_pessoa = ''
        if session['usuario'] == 'rafael':
            nome_pessoa = 'Rafael'
        elif session['usuario'] == 'maria':
            nome_pessoa = 'Maria dos Santos'
        return render_template('area_logada.html', nome=nome_pessoa)
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
app.run(debug=True)

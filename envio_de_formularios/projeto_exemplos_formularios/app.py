from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    nome = request.form.get("nome")
    idade = request.form.get("idade")
    if nome == None or idade == None:
        return render_template('formulario.html')
    else:
        return f"O nome é: {nome}, e a idade é: {idade}. Estamos Felizes de ter você conosco!!!!"

app.run(debug=True)

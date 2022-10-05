from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    resposta = render_template('pagina.html')
    return resposta



app.run(debug=True)
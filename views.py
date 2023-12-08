from flask import render_template,request, redirect,url_for, flash, session, send_from_directory
from app import app, db
from models.modelos import Usuarios, Produtos

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro_usuario', methods= ['GET', 'POST'])
def cadastro_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        endereco = request.form['endereco']
        numcasa = request.form['numcasa']
        bairro = request.form['bairro']
        senha = request.form['senha']

        if nome and email and endereco and numcasa and bairro and senha:
            novo_usuario = Usuarios(nome, email, endereco, numcasa, bairro, senha)
            db.session.add(novo_usuario)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('novo_usuario.html')
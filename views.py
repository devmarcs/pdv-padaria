from flask import render_template,request, redirect,url_for, flash, session, send_from_directory
from flask_login import login_user, logout_user,current_user, login_required
from app import app, db
from models.modelos import Usuarios, Produtos


@app.route('/')
def index():
    return render_template('login.html')



@app.route('/menu', methods=['GET', 'POST'])
@login_required
def menu():
    return render_template('menu.html')



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




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        usuario = Usuarios.query.filter_by(email=email).first()

        if usuario and usuario.verifica_senha(senha):
            login_user(usuario)
            return redirect(url_for('menu'))
        
        flash('Credenciais inválidas', 'error')
    
    return render_template('login.html')



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

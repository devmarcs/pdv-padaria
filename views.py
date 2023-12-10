from flask import render_template,request, redirect,url_for, flash, session, send_from_directory
from flask_login import login_user, logout_user,current_user, login_required
from sqlalchemy.exc import IntegrityError
from app import app, db
from models.modelos import Usuarios, Produtos
from app import bcrypt

@app.route('/')
def index():
    return render_template('login.html')



@app.route('/menu/<int:id>', methods=['GET', 'POST'])
@login_required
def menu(id):
    usuario = Usuarios.query.filter_by(id=id).first()
    return render_template('menu.html', usuario=usuario)




#================ Cadastro Usuário ================
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
            try:
                novo_usuario = Usuarios(nome, email, endereco, numcasa, bairro, senha)
                db.session.add(novo_usuario)
                db.session.commit()
                flash('Usuário Cadastrado com sucesso!')
                return redirect(url_for('index'))
            except IntegrityError:
                db.session.rollback()
                flash('Erro: Já existe um usuário cadastrado com esse e-mail')
    return render_template('novo_usuario.html')


#============= Tela de editar Usuários ===================
@app.route('/editar_usuario/<int:id>')  
@login_required
def editar_usuario(id):
    usuario = Usuarios.query.filter_by(id=id).first()
    return render_template('editar_usuario.html',usuario=usuario)


#================= Função que faz a Edição de Usuário ====================
@app.route('/editar_user', methods= ['POST']) 
@login_required
def editar_user():
    usuario = Usuarios.query.filter_by(id=request.form['id']).first()
    usuario.nome = request.form['nome']
    usuario.email = request.form['email']
    usuario.endereco = request.form['endereco']
    usuario.numcasa = request.form['numcasa']
    usuario.bairro = request.form['bairro']
    nova_senha = request.form['senha']
    if nova_senha:
        senha_hash = bcrypt.generate_password_hash(nova_senha).decode('utf-8')
        usuario.senha = senha_hash
        
    db.session.add(usuario)
    db.session.commit()
    flash('Usuário atualizado com sucesso!')
    return redirect(url_for('editar_usuario', id=current_user.id))



@app.route('/dados_usuario/<int:id>')  
def dados_usuario(id):
    usuario = Usuarios.query.filter_by(id=id).first()
    return render_template('usuario.html',usuario=usuario)



#========== Função que deleta usuário ==================
@app.route('/deletar_usuario/<int:id>')
@login_required
def deletar_usuario(id):
    Usuarios.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Usuário deletado com sucesso!')
    return redirect(url_for('index'))




#================= Login do Usuário ====================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        usuario = Usuarios.query.filter_by(email=email).first()

        if usuario and usuario.verifica_senha(senha):
            login_user(usuario)
            return redirect(url_for('menu', id=current_user.id))
        
        flash('Credenciais inválidas', 'error')
    
    return render_template('login.html')


#========== Encerrar Sessão ============
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


#================ Cadastro de Produto ==================
@app.route('/cadastro_produto', methods= ['GET', 'POST'])
@login_required
def cadastro_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['categoria']
        preco = request.form['preco']
        quantidade = request.form['quantidade']
        descricao = request.form['descricao']
        

        if nome and categoria and preco and quantidade and descricao:
            novo_produto = Produtos(nome, categoria, preco, quantidade,  descricao)
            db.session.add(novo_produto)
            db.session.commit()
            flash('Produto cadastrado com sucesso!' )
            return redirect(url_for('cadastro_produto', id=current_user.id))
    return render_template('novo_produto.html')


#===== Tela editar produtos =====
@app.route('/editar_produto/<int:id>')
@login_required
def editar_produtos(id):
    
    produto = Produtos.query.filter_by(id=id).first()
    return render_template('editar_produto.html',produto= produto)

#===== Função que faz a edição dos produtos =====
@app.route('/atualizar_produto', methods= ['POST']) 
@login_required
def atualizar_produto():
    produto = Produtos.query.filter_by(id=request.form['id']).first()
    produto.nome = request.form['nome']
    produto.categoria = request.form['categoria']
    produto.preco = request.form['preco']
    produto.quantidade = request.form['quantidade']
    produto.descricao = request.form['descricao']

    db.session.add(produto)
    db.session.commit()
    flash('Produto atualizado com sucesso!')
    return redirect(url_for('editar_produtos', id=current_user.id))




#========================== Listar o produto expecífico ====================
@app.route('/produtos/<int:id>')
@login_required
def produto(id):
    produto = Produtos.query.filter_by(id=id).first()
    return render_template('produto.html', produtos=produto)


#========== Deletar o produto ===================
@app.route('/deletar_produto/<int:id>')
@login_required
def deletar_produto(id):
    Produtos.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Produto deletado com sucesso!')
    return redirect(url_for('menu', id=current_user.id))

#================ Listar todos os produtos =====================
@app.route('/produtos')
@login_required
def produtos():
    lista = Produtos.query.order_by(Produtos.id)
    return render_template('lista_produtos.html',produtos= lista)

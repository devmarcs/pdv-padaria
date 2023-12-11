from app import db, login_manager, bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id):
    return Usuarios.query.filter_by(id=user_id).first()



class Usuarios(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    endereco = db.Column(db.String(100), nullable=False)
    numcasa = db.Column(db.Integer, nullable=False)
    bairro = db.Column(db.String(60), nullable=False)
    senha = db.Column(db.String(12), nullable=False)

    def __init__(self, nome, email, endereco, numcasa, bairro, senha):
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.numcasa = numcasa
        self.bairro = bairro
        self.senha = generate_password_hash(senha)

    def set_senha(self, senha):
        self.senha = bcrypt.generate_password_hash(senha).decode('utf-8')

    def verifica_senha(self, senha):
        return bcrypt.check_password_hash(self.senha, senha)

    '''def verifica_senha(self, chave):
        return check_password_hash(self.senha, chave)'''

    def __repr__(self):
        return '<Name %r>' % self.nome
    


class Produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Integer, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(200), nullable=False)

    def __init__(self, nome, categoria, preco, quantidade, descricao):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade
        self.descricao = descricao 

    def __repr__(self):
        return '<Name %r>' % self.nome
    
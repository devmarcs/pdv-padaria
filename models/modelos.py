from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id):
    return Usuarios.query.filter_by(id=user_id)



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

    def verifica_senha(self, sen):
        return check_password_hash(self.senha, sen  )

    def __repr__(self):
        return '<Name %r>' % self.nome
    


class Produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False, unique=True)
    categoria = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(60), nullable=False)

    def __init__(self, nome, categoria, preco, descricao):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.descricao = descricao 

    def __repr__(self):
        return '<Name %r>' % self.nome
    
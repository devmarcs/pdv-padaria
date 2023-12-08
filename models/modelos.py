from config import db

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False, unique=True)
    idade = db.Column(db.Integer, nullable=False)
    endereco = db.Column(db.String(100), nullable=False)
    numcasa = db.Column(db.Integer, nullable=False)
    bairro = db.Column(db.String(60), nullable=False)

    def __init__(self, nome, idade, endereco, numcasa, bairro):
        self.nome = nome
        self.idade = idade
        self.enderco = endereco
        self.numcasa = numcasa
        self.bairro = bairro

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
        self.idade = categoria
        self.preco = preco
        self.descricao = descricao 

    def __repr__(self):
        return '<Name %r>' % self.nome
    
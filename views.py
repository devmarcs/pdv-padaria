from flask import render_template,request, redirect,url_for, flash, session, send_from_directory
from app import app
from models.modelos import Usuarios, Produtos

@app.route('/')
def index():
    return render_template('index.html')
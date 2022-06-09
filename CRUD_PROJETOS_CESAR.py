from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# # app.config['SECRET_KEY'] = "1234"
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:mysqladmin@localhost/crud_projeto"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:mysqladmin@localhost/aulanext?createDataBaseifNotExist=true"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from Routes.Projetos_Routes import setup_route
# import Models.Projeto_Entity

class Projeto_Entity(db.Model):
    
    # atributos para teste. apague depois.
    id = db.Column('projeto_id', db.Integer, primary_key = True)
    nome = db.Column(db.String())
    documento = db.Column(db.String())
    imoveis_proprios = db.Column(db.String())
    imoveis_em_locacao = db.Column(db.String())

    def __init__(self, nome, documento, imoveis_proprios, imoveis_em_locacao):
        self.nome = nome
        self.documento = documento
        self.imoveis_proprios = imoveis_proprios
        self.imoveis_em_locacao = imoveis_em_locacao

setup_route(app)

if __name__ == '__main__':
    app.run(debug=False)
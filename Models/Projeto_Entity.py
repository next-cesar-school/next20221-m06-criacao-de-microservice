from flask_sqlalchemy import SQLAlchemy
from CRUD_PROJETOS_CESAR import db

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
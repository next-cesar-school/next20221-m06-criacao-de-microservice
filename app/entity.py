from app.config_db import db

class Entity_project(db.Model):
    
    # atributos para teste. apague depois.
    id = db.Column('projeto_id', db.Integer, primary_key = True)
    nome = db.Column(db.String(255))
    documento = db.Column(db.String(255))
    imoveis_proprios = db.Column(db.String(255))
    imoveis_em_locacao = db.Column(db.String(255))

	# no problem here
    def __init__(self, nome, documento, imoveis_proprios, imoveis_em_locacao):
        self.nome = nome
        self.documento = documento
        self.imoveis_proprios = imoveis_proprios
        self.imoveis_em_locacao = imoveis_em_locacao
from app.config_db import db

# class Entity_project(db.Model):
    
#     # atributos para teste. apague depois.
#     id = db.Column('projeto_id', db.Integer, primary_key = True)
#     nome = db.Column(db.String(255))
#     documento = db.Column(db.String(255))
#     imoveis_proprios = db.Column(db.String(255))
#     imoveis_em_locacao = db.Column(db.String(255))

# 	# no problem here
#     def __init__(self, nome, documento, imoveis_proprios, imoveis_em_locacao):
#         self.nome = nome
#         self.documento = documento
#         self.imoveis_proprios = imoveis_proprios
#         self.imoveis_em_locacao = imoveis_em_locacao


class ProjetoEntity(db.Model):
    __tablename__ = 'projetos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    centro_custo = db.Column(db.String(50))
    data_inicio = db.Column(db.String(10))
    data_fim = db.Column(db.String(10))
    status = db.Column(db.String(50))
    flag = db.Column(db.String(50))
    id_gerente = db.Column(db.Integer)

    def __init__(self, nome, centro_custo, data_inicio, data_fim, status, flag, id_gerente):
        self.nome = nome
        self.centro_custo = centro_custo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = status
        self.flag = flag
        self.id_gerente = id_gerente

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'centro_custo': self.centro_custo,
            'data_inicio': self.data_inicio,
            'data_fim': self.data_fim,
            'status': self.status,
            'flag': self.flag,
            'id_gerente': self.id_gerente
        }

    @classmethod
    def find_projeto(cls, id):
        # SELECT * FROM projetos WHERE id(do db) = id(do parametro)
        projeto = cls.query.filter_by(id=id).first()
        if projeto:
            return projeto
        return None
    
    def save_projeto(self):
        db.session.add(self)
        db.session.commit()

    def update_projeto(self, nome, centro_custo, data_inicio, data_fim, status, flag, id_gerente):
        self.nome = nome
        self.centro_custo = centro_custo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = status
        self.flag = flag
        self.id_gerente = id_gerente
    
    def delete_projeto(self):
        db.session.delete(self)
        db.session.commit()
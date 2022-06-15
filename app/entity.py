from app.config_db import db
from sqlalchemy import ForeignKey

#colocar methodos comuns aqui
class CommonMethods():
	# @classmethod
	def find_project(cls, id):
		# SELECT * FROM projects WHERE id(do db) = id(do parametro)
		project = cls.query.filter_by(id=id).first()
		if project:
			return project
		return None

class ProjectEntity(db.Model, CommonMethods):
	__tablename__ = 'projects'

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(100))
	id_centro_custo = db.Column(db.Integer, ForeignKey('cost_center.id'))
	data_inicio = db.Column(db.String(10))
	data_fim = db.Column(db.String(10))
	status = db.Column(db.Enum('iniciado', 'on-hold', 'finalizado', 'em aprovação'))
	flag = db.Column(db.Enum('vermelho', 'amarelo', 'verde'))
	id_gerente = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
	
	def __init__(self, nome, id_centro_custo, data_inicio, data_fim, status, flag, id_gerente):
		self.nome = nome
		self.id_centro_custo = id_centro_custo
		self.data_inicio = data_inicio
		self.data_fim = data_fim
		self.status = status
		self.flag = flag
		self.id_gerente = id_gerente

	def json(self):
		return {
            'id': self.id,
            'nome': self.nome,
            'id_centro_custo': self.id_centro_custo,
            'data_inicio': self.data_inicio,
            'data_fim': self.data_fim,
            'status': self.status,
            'flag': self.flag,
            'id_gerente': self.id_gerente
        }

	# @classmethod
	# def find_project(cls, id):
	# 	# SELECT * FROM projects WHERE id(do db) = id(do parametro)
	# 	project = cls.query.filter_by(id=id).first()
	# 	if project:
	# 		return project
	# 	return None

	super().find_project()
	
	def save_project(self):
		db.session.add(self)
		db.session.commit()

	def update_project(self, nome, id_centro_custo, data_inicio, data_fim, status, flag, id_gerente):
		self.nome = nome
		self.id_centro_custo = id_centro_custo
		self.data_inicio = data_inicio
		self.data_fim = data_fim
		self.status = status
		self.flag = flag
		self.id_gerente = id_gerente
    
	def delete_project(self):
		db.session.delete(self)
		db.session.commit()

# User Entity
class UsersEntity(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	primeiro_nome = db.Column(db.String(100))
	ultimo_nome = db.Column(db.String(50))
	data_nascimento = db.Column(db.String(10))
	cargo = db.Column(db.String(10))
	matricula = db.Column(db.String(50), unique=True)
	status = db.Column(db.Enum('ativo', 'inativo'))
	id_centro_custo = db.Column(db.Integer, ForeignKey('cost_center.id'))

	gerente = db.relationship (ProjectEntity)

	def __init__(self, primeiro_nome, ultimo_nome, data_nascimento, cargo, matricula, status, id_centro_custo):
		self.primeiro_nome = primeiro_nome
		self.ultimo_nome = ultimo_nome
		self.data_nascimento = data_nascimento
		self.cargo = cargo
		self.matricula = matricula
		self.status = status
		self.id_centro_custo = id_centro_custo

	def json(self):
		return {
			'id': self.id,
			'primeiro_nome': self.primeiro_nome,
			'ultimo_nome': self.ultimo_nome,
			'data_nascimento': self.data_nascimento,
			'cargo': self.cargo,
			'matricula': self.matricula,
			'status': self.status,
			'id_centro_custo': self.id_centro_custo
		}

	@classmethod
	def find_user(cls, id):
        # igual a SELECT * FROM users WHERE id(do db) = id(do parametro)
		user = cls.query.filter_by(id=id).first()
		if user:
			return user
		return None

	@classmethod
	def find_user_matricula(cls, matricula):
        # igual a SELECT * FROM users WHERE id(do db) = id(do parametro)
		user_matricula = cls.query.filter_by(matricula=matricula).first()
        
		if user_matricula:
			return user_matricula
		return None
    
	def save_user(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def find_user_matricula(cls, matricula):
		# igual a SELECT * FROM users WHERE id(do db) = id(do parametro)
		user_matricula = cls.query.filter_by(matricula=matricula).first()
		
		if user_matricula:
			return user_matricula
		return None
	
	def save_user(self):
		db.session.add(self)
		db.session.commit()

	def update_user(self, primeiro_nome, ultimo_nome, data_nascimento, cargo, matricula, status, id_centro_custo):
		self.primeiro_nome = primeiro_nome
		self.ultimo_nome = ultimo_nome
		self.data_nascimento = data_nascimento
		self.cargo = cargo
		self.matricula = matricula
		self.status = status
		self.id_centro_custo = id_centro_custo
	
	def delete_user(self):
		db.session.delete(self)
		db.session.commit()


# Centro de Custo Entity
class CostCenterEntity(db.Model):
	__tablename__ = 'cost_center'

	id = db.Column(db.Integer, primary_key=True)
	setor = db.Column(db.String(100), unique=True)

	user = db.relationship (UsersEntity)
	project = db.relationship (ProjectEntity)

	
	def __init__(self, setor):
		self.setor = setor

	def json(self):
		return {
			'id' : self.id,
			'setor': self.setor            
		}

	@classmethod
	def find_center(cls, id):
		# igual a SELECT * FROM users WHERE id(do db) = id(do parametro) ,,
		center = cls.query.filter_by(id=id).first()
		if center:
			return center
		return None
	
	@classmethod
	def find_center_setor(cls, setor):
		# igual a SELECT * FROM users WHERE id(do db) = id(do parametro)
		center_setor = cls.query.filter_by(setor=setor).first()
		
		if center_setor:
			return center_setor
		return None

	def save_center(self):
		db.session.add(self)
		db.session.commit()

	def update_center(self, setor):
		self.setor = setor

	def delete_center(self):
		db.session.delete(self)
		db.session.commit()

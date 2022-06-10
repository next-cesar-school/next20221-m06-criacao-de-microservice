# from Routes.Projetos_Routes import Projetos, Projeto

def setup_general_config(app):
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Ai.471471@localhost/project_manager'

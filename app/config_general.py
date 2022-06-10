def setup_general_config(app):
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:mysqladmin@localhost/project_manager'

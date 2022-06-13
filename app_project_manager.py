from flask import Flask

from app.config_general import setup_general_config
from app.config_db import setup_db, db
from app.setup_route import IndexEntity, Projects, Project, Users, User, Centers, Center
from flask_restful import Api

app = Flask(__name__)

setup_general_config(app)
setup_db(app)


api = Api(app)

api.add_resource(IndexEntity, '/index' )
api.add_resource(Projects, '/projects')
api.add_resource(Project, '/projects/<int:id>')
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:id>')
api.add_resource(Centers, '/costcenters')
api.add_resource(Center, '/costcenters/<int:id>')

# cria o banco de dados e tabelas do anrquivo 'entity.py'
@app.before_first_request
def init_db():
	db.create_all()

if __name__ == '__main__':
	app.run(debug=True)
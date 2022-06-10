from flask import Flask

from app.config_general import setup_general_config
# from app.setup_route import setup_route
from app.config_db import setup_db, db
from app.setup_route import Projetos, Projeto, IndexEntity
from flask_restful import Api

app = Flask(__name__)

setup_general_config(app)
setup_db(app)
# setup_route(app)

api = Api(app)

api.add_resource(Projetos, '/projetos')
api.add_resource(Projeto, '/projetos/<int:id>')
api.add_resource(IndexEntity, '/index' )

# cria o banco de dados e tabelas do anrquivo 'entity.py'
@app.before_first_request
def innit_db():
	db.create_all()

if __name__ == '__main__':
	app.run(debug=True)
from flask import request, flash, url_for, redirect, render_template, Response
from app.entity import ProjetoEntity
from flask_restful import Resource
import json


# def setup_route(app):
# # Função visão geral.
# @app.route('/index')
# def index():
# 	# return "E aí essa galera?"
# 	return render_template('show_index.html', projeto=Entity_project.query.order_by(Entity_project.id).all())
# 	# return json

# @app.route('/index/projects, methods=["GET"]')
# def select_projects():
# 	dic_output_msg = {"user": None,
# 				  "message": "Fim listagem"}
# 	show_projects = Entity_project.query.order_by(Entity_project.id).all()
# 	dic_output_msg["projects"] = [user.to_json() for user in show_projects]
# 	return Response(json.dumps(dic_output_msg))

class IndexEntity(Resource):
    def get(self):
        return 'oi'

class Projetos(Resource):

    def get(self):
        return {'projetos': [projeto.json() for projeto in ProjetoEntity.query.all()]}

    def post(self):
        dados = request.get_json()
        projeto = ProjetoEntity(**dados)
        try:
            projeto.save_projeto()
        except:
            # Internal Server Error
            return {'message': 'An internal error occurred trying to save projeto.'}, 500
        return projeto.json()


class Projeto(Resource):
    def get(self, id):
        projeto = ProjetoEntity.find_projeto(id)
        if projeto:
            return projeto.json()
        return {'message': 'Projeto not found.'}, 404

    def post(self, id):
        if ProjetoEntity.find_projeto(id):
            # Bad request
            return {'message': 'Projeto id {} already exists.'.format(id)}, 400

        dados = request.get_json()
        projeto = ProjetoEntity(**dados)
        projeto.id = id
        try:
            projeto.save_projeto()
        except:
            # Internal Server Error
            return {'message': 'An internal error occurred trying to save projeto.'}, 500
        return projeto.json()

    def put(self, id):
        dados = request.get_json()
        projeto = ProjetoEntity.find_projeto(id)
        if projeto:
            projeto.update_projeto(**dados)
            try:
                projeto.save_projeto()
            except:
                # Internal Server Error
                return {'message': 'An internal error occurred trying to save projeto.'}, 500
            return projeto.json(), 200
        return {'message': 'Projeto not found.'}, 404

    def delete(self, id):
        projeto = ProjetoEntity.find_projeto(id)
        if projeto:
            try:
                projeto.delete_projeto()
            except:
                # Internal Server Error
                return {'message': 'An internal error occurred trying to delete projeto.'}, 500
            return{'message': 'Projeto deleted.'}
        return {'message': 'Projeto not found.'}, 404
# 		# READ
# @app.route("/users", methods=["GET"])
# def select_users():
#     dic_output_msg = {"user": None,
#                       "mensage": "Fim listagem"}
#     users_select = User.query.all()
        # dic_output_msg["user"] = [user.to_json() for user in users_select]
        # return Response(json.dumps(dic_output_msg))


# @app.route("/user/<id>", methods=["GET"])
# def select_user(id):
#     dic_output_msg = {"user": None,
#                       "mensage": "Fim listagem"}
#     user_select = User.query.filter_by(id=id).first()
#     dic_output_msg["user"] = user_select.to_json()
#     return Response(json.dumps(dic_output_msg))

# # CREATE
# @app.route("/user", methods=["POST"])
# def create_user():
#     dic_output_msg = {"user": None,
#                       "mensage": "Cadastro criado com sucesso"}
#     try:
#         data = request.get_json()
#         user = User(name=data["name"], email=data["email"])
#         dic_output_msg["user"] = user.to_json()
#         db.session.add(user)
#         db.session.commit()
#         return Response(json.dumps(dic_output_msg))
#     except:
#         return Response(json.dumps("Erro ao criar cadastro!"))

# 	# DELETE
# @app.route("/user/<id>", methods=["DELETE"])
# def delete_user(id):
#     dic_output_msg = {"user": None,
#             "mensage": "Cadastro deletado com sucesso"}
#     try:
#         user_delete = User.query.filter_by(id=id).first()
#         dic_output_msg["user"] = user_delete.to_json()
#         db.session.delete(user_delete)
#         db.session.commit()
#         return Response(json.dumps(dic_output_msg))
#     except:
#         return Response(json.dumps("Erro ao deletar cadastro"))
    # return render pass

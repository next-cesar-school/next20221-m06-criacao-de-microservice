from flask import request
from flask_restful import Resource, Api
from app.entity import ProjectEntity, UsersEntity, CostCenterEntity, ProjectUserEntity
from app.config_db import db


def setup_route(app):

    # Este rota é para designar o menu inicial. Feito no Angular?
    class IndexEntity(Resource):
        def get(self):
            return 'oi'

    class Projects(Resource):

        def get(self):
            return {'projects': [project.json() for project in ProjectEntity.query.all()]}

        def post(self):
            try:
                data = request.get_json()
                project = ProjectEntity(**data)
                project.save_project()
                return project.json()

            except:
                # Internal Server Error
                return {'message': 'An internal error occurred trying to save project.'}, 500

    class Project(Resource):

        def get(self, id):
            # error_id_not_int(id)
            try:
                int(id) == id
                project = ProjectEntity.find_project(id)
                if project:
                    return project.json()
                return {'message': 'Project not found.'}, 404

            except ValueError:
                return {'message': f'Oops! This ID {id} is not valid'}, 400

        def post(self, id):
            # error_id_not_int(id)
            try:
                int(id) == id
                int(id) > 0
                if ProjectEntity.find_project(id):
                    # Bad request
                    return {'message': f'Project id {id} already exists.'}, 400

                data = request.get_json()
                project = ProjectEntity(**data)
                project.id = id
                project.save_project()
                return project.json()

            except ValueError:
                return {'message': f'Oops! This ID {id} is not valid'}, 400
            except:
                # Internal Server Error
                return {'message': 'An internal error occurred trying to save project.'}, 500

        def put(self, id):
            # error_id_not_int(id)
            try:
                int(id) == id
                data = request.get_json()
                project = ProjectEntity.find_project(id)

                if project:
                    project.update_project(**data)
                    project.save_project()
                    return project.json(), 200
                return {'message': 'Project not found.'}, 404

            except ValueError:
                return {'message': f'Oops! This ID {id} is not valid'}, 400
            except:
                # Internal Server Error
                return {'message': 'An internal error occurred trying to save project.'}, 500

        def delete(self, id):
            # error_id_not_int(id)
            try:
                int(id) == id
                project = ProjectEntity.find_project(id)

                if project:
                    project.delete_project()
                    return{'message': 'Project deleted.'}
                return {'message': 'Project does not exist.'}, 404

            except ValueError:
                return {'message': f'Oops! This ID {id} is not valid'}, 400
            except:
                # Internal Server Error
                return {'message': 'An internal error occurred trying to delete project.'}, 500

    class Users(Resource):

        def get(self):
            return {'users': [user.json() for user in UsersEntity.query.all()]}

        def post(self):
            try:
                data = request.get_json()
                user = UsersEntity(**data)

                if UsersEntity.find_user_matricula(user.matricula):
                    return {'message': f'User matricula {user.matricula} already exists.'}, 400
                user.save_user()
                return user.json()

            except:
                # Internal Server Error
                return {'message': 'An internal error occurred trying to save User.'}, 500

    class User(Resource):

        def get(self, id):
            # error_id_not_int(id)
            try:
                int(id) == id
                user = UsersEntity.find_user(id)

                if user:
                    return user.json()
                return {'message': 'User not found.'}, 404

            except ValueError:
                return {'message': f'Oops! This User ID {id} is not valid'}, 400

        def post(self, id):
            # error_id_not_int(id)
            try:
                int(id) == id
                int(id) > 0
                if UsersEntity.find_user(id):
                    # Bad request
                    return {'message': f'User ID {id} already exists.'}, 400

                data = request.get_json()
                user = UsersEntity(**data)

                if UsersEntity.find_user_matricula(user.matricula):
                    return {'message': f'User matricula {user.matricula} already exists.'}, 400

                user.id = id
                user.save_user()
                return user.json(), 200

            except ValueError:
                return {'message': f'Oops! This User ID {id} is not valid'}, 400
            except:
                # Internal Server Error
                return {'message': 'An internal error occurred trying to post User.'}, 500

        def put(self, id):
            # error_id_not_int(id)
            try:
                int(id) == id
                data = request.get_json()
                user = UsersEntity.find_user(id)

                if user:
                    user.update_user(**data)
                    user.save_user()
                    return user.json(), 200
                return {'message': 'User not found.'}, 404

            except ValueError:
                return {'message': f'Oops! This User ID {id} is not valid'}, 400
            except:
                # Internal Server Error
                return {'message': 'An internal error occurred trying to save user.'}, 500

        def delete(self, id):
            # error_id_not_int(id)
            try:
                int(id) == id
                user = UsersEntity.find_user(id)

                if user:
                    user.delete_user()
                    return{'message': 'User deleted.'}
                return {'message': 'User does not exist.'}, 404

            except ValueError:
                return {'message': f'Oops! This User ID {id} is not valid'}, 400
            except:
                # Internal Server Error
                return {'message': 'An internal error occurred trying to delete user.'}, 500

    class Centers(Resource):
        def get(self):
            return {'Cost Centers': [center.json() for center in CostCenterEntity.query.all()]}

        def post(self):
            try:
                data = request.get_json()
                center = CostCenterEntity(**data)
                if CostCenterEntity.find_center_setor(center.setor):
                    return {'message': f'Cost center sector {center.setor} already exists.'}, 400
                center.save_center()
                return center.json()
            except:
                # Internal Server Error
                return {'message': 'An internal error occurred trying to save cost center.'}, 500

    class Center(Resource):
        def get(self, id):
            # error_id_not_int(id)
            try:
                int(id) == id
                center = CostCenterEntity.find_center(id)
                if center:
                    return center.json()
                return {'message': 'Cost Center not found.'}, 404
            except ValueError:
                return {'message': f'Oops! This Cost Center ID {id} is not valid'}, 400

        def post(self, id):
            # error_id_not_int(id)
            try:
                int(id) == id
                int(id) > 0
                if CostCenterEntity.find_center(id):
                    # Bad request
                    return {'message': f'Cost center ID {id} already exists.'}, 400
                data = request.get_json()
                center = CostCenterEntity(**data)
                if CostCenterEntity.find_center_setor(center.setor):
                    return {'message': f'Cost Center sector {center.setor} already exists.'}, 400
                center.id = id
                center.save_center()
                return center.json()
            except ValueError:
                return {'message': f'Oops! This Cost Center ID {id} is not valid'}, 400
            except:
                # Internal Server Error
                return {'message': 'An internal error occurred trying to save Cost Center.'}, 500

        def put(self, id):
            # error_id_not_int(id)
            try:
                int(id) == id
                data = request.get_json()
                center = CostCenterEntity.find_center(id)
                if center:
                    center.update_center(**data)
                    center.save_center()
                    return center.json(), 200
                return {'message': 'Cost Center not found.'}, 404
            except ValueError:
                return {'message': f'Oops! This Cost Center ID {id} is not valid'}, 400
            except:
                # Internal Server Error
                return {'message': 'An internal error occurred trying to save Cost Center.'}, 500

        def delete(self, id):
            # rror_id_not_int(id)
            try:
                int(id) == id
                center = CostCenterEntity.find_center(id)
                if center:
                    center.delete_center()
                    return{'message': 'Cost Center deleted.'}
                return {'message': 'Cost Center not found.'}, 404
            except ValueError:
                return {'message': f'Oops! This Cost Center ID {id} is not valid'}, 400
            except:
                # Internal Server Error
                return {'message': 'An internal error occurred trying to delete Cost Center.'}, 500

    class ProjectsUsers(Resource):

        def get(self):
            return {'projects users': [project_user.json() for project_user in ProjectUserEntity.query.all()]}

    class ProjectsIDUsers(Resource):

        def get(self, id):
            try:
                int(id) == id
                project_user = ProjectUserEntity.find_project_all_users(id)
                list_users = [item.user_id for item in project_user]
                dict_users = {}
                contador = 1
                for id_user in list_users:
                    name = UsersEntity.find_user(id_user)
                    dict_users['user ' + str(contador)] = name.json()
                    contador += 1
                return {f'USERS FROM PROJECT ID {id}': dict_users}
            except ValueError:
                return {'message': f'Oops! This Project ID {id} is not valid'}, 400
            except:
                return {'message': 'Project not found.'}, 500

        def post(self, id):
            try:
                int(id) == id
                data = request.get_json()
                project_user = ProjectUserEntity(**data)
                project_user.project_id = id
                project_user.save_project_user()
                return project_user.json()
            except ValueError:
                return {'message': f'Oops! This Project ID {id} is not valid'}, 400
            except:
                # Internal Server Error
                return {'message': 'An internal error occurred trying to save user in project.'}, 500
            
        
        def delete(self, id, id2):

            try:
                int(id) == id
                int(id2) == id2
                if int(id) <= 0:
                    return {'message': f'Oops! The Project ID {id} is not valid'}, 400
                elif int(id2) <= 0:
                    return {'message': f'Oops! The User ID {id2} is not valid'}, 400
                project_user = ProjectUserEntity.find_project_by_user(id, id2)
                if project_user:
                    project_user.delete_project_user()
                    return{'message': f'User ID {id2} deleted from Project ID {id}.'}
                return {'message': 'User ID not found in this Project.'}, 404
            except ValueError:
                try:
                    int(id) == id
                    return {'message': f'Oops! The User ID {id2} is not valid'}, 400
                except:
                    return {'message': f'Oops! The Project ID {id} is not valid'}, 400
            except:
                # Internal Server Error
                return {'message': f'An internal error occurred trying to delete User ID {id2} from Project ID {id}.'}, 500


# ENDPOINTS:
    api = Api(app)
    api.add_resource(IndexEntity, '/index', '/index/')
    api.add_resource(Projects, '/projects', '/projects/')
    api.add_resource(Project, '/projects/<id>', '/projects/<id>/')
    api.add_resource(Users, '/users', '/users/')
    api.add_resource(User, '/users/<id>', '/users/<id>/')
    api.add_resource(Centers, '/costcenters', '/costcenters/')
    api.add_resource(Center, '/costcenters/<id>', '/costcenters/<id>/')
    api.add_resource(ProjectsUsers, '/projects/users', '/projects/users/')
    api.add_resource(ProjectsIDUsers, '/projects/<id>/users',
                     '/projects/<id>/users/', '/projects/<id>/users/<id2>', '/projects/<id>/users/<id2>/')

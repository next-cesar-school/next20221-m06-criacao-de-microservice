from flask import render_template, request
from flask_restful import Resource, Api
from master.entity import ProjectEntity, UsersEntity, CostCenterEntity, ProjectUserEntity
import master.constants as const


def setup_route(app):

    @app.route('/index')
    def index():
        return render_template('show_index.html')

    class IndexEntity(Resource):
        def index():
            return render_template('show_index.html')

    class Projects(Resource):

        def get(self):
            return {'Projects': [project.json() for project in ProjectEntity.query.all()]}, 200

        def post(self):
            try:
                data = request.get_json()
                project = ProjectEntity(**data)
                project.save_project()
                return project.json(), 200

            except:
                return const.GENERAL_INTERNAL_ERROR_SAVE

    class Project(Resource):

        def get(self, id):

            try:
                int(id) == id
                project = ProjectEntity.find_project(id)
                if project:
                    return project.json(), 200
                return const.GENERAL_ID_NOT_FOUND

            except ValueError:
                return const.GENERAL_ID_NOT_FOUND

        def post(self, id):

            try:
                int(id) == id
                int(id) > 0
                if ProjectEntity.find_project(id):
                    return const.GENERAL_ID_ALREADY_EXISTS

                data = request.get_json()
                project = ProjectEntity(**data)
                project.id = id
                project.save_project()
                return project.json(), 200

            except ValueError:
                return const.GENERAL_ID_NOT_FOUND
            except:
                return const.GENERAL_INTERNAL_ERROR_SAVE

        def put(self, id):
            try:
                int(id) == id
                data = request.get_json()
                project = ProjectEntity.find_project(id)

                if project:
                    project.update_project(**data)
                    project.save_project()
                    return project.json(), 200
                return const.GENERAL_ID_NOT_FOUND

            except ValueError:
                return const.GENERAL_ID_NOT_FOUND
            except:
                return const.GENERAL_INTERNAL_ERROR_SAVE

        def delete(self, id):

            try:
                int(id) == id
                project = ProjectEntity.find_project(id)

                if project:
                    project.delete_project()
                    return const.GENERAL_ID_DELETED
                return const.GENERAL_ID_NOT_FOUND

            except ValueError:
                return const.GENERAL_ID_NOT_FOUND
            except:
                return const.GENERAL_INTERNAL_ERROR_DELETE

    class Users(Resource):

        def get(self):
            return {'Users': [user.json() for user in UsersEntity.query.all()]}, 200

        def post(self):
            try:
                data = request.get_json()
                user = UsersEntity(**data)

                if UsersEntity.find_user_registration_number(user.registration_number):
                    return const.USER_REGISTRATION_NUMBER_ALREADY_EXISTS
                user.save_user()
                return user.json(), 200

            except:

                return const.GENERAL_INTERNAL_ERROR_SAVE

    class User(Resource):

        def get(self, id):

            try:
                int(id) == id
                user = UsersEntity.find_user(id)

                if user:
                    return user.json(), 200
                return const.GENERAL_ID_NOT_FOUND

            except ValueError:
                return const.GENERAL_ID_NOT_FOUND

        def post(self, id):

            try:
                int(id) == id
                int(id) > 0
                if UsersEntity.find_user(id):
                    return const.GENERAL_ID_ALREADY_EXISTS

                data = request.get_json()
                user = UsersEntity(**data)

                if UsersEntity.find_user_registration_number(user.registration_number):
                    return const.USER_REGISTRATION_NUMBER_ALREADY_EXISTS

                user.id = id
                user.save_user()
                return user.json(), 200

            except ValueError:
                return const.GENERAL_ID_NOT_FOUND
            except:
                return const.GENERAL_INTERNAL_ERROR_SAVE

        def put(self, id):
            try:
                int(id) == id
                data = request.get_json()
                user = UsersEntity.find_user(id)

                if user:
                    user.update_user(**data)
                    user.save_user()
                    return user.json(), 200
                return const.GENERAL_ID_NOT_FOUND

            except ValueError:
                return const.GENERAL_ID_NOT_FOUND
            except:

                return const.GENERAL_INTERNAL_ERROR_SAVE

        def delete(self, id):

            try:
                int(id) == id
                user = UsersEntity.find_user(id)

                if user:
                    user.delete_user()
                    return const.GENERAL_ID_DELETED
                return const.GENERAL_ID_NOT_FOUND

            except ValueError:
                return const.GENERAL_ID_NOT_FOUND
            except:

                return const.GENERAL_INTERNAL_ERROR_DELETE

    class Centers(Resource):
        def get(self):
            return {'Cost Centers': [center.json() for center in CostCenterEntity.query.all()]}, 200

        def post(self):
            try:
                data = request.get_json()
                center = CostCenterEntity(**data)
                if CostCenterEntity.find_center_department(center.department_name):
                    return const.COST_CENTER_DEPARTMENT_ALREADY_EXISTS
                center.save_center()
                return center.json(), 200
            except:
                return const.GENERAL_INTERNAL_ERROR_SAVE

    class Center(Resource):
        def get(self, id):

            try:
                int(id) == id
                center = CostCenterEntity.find_center(id)
                if center:
                    return center.json(), 200
                return const.GENERAL_ID_NOT_FOUND
            except ValueError:
                return const.GENERAL_ID_NOT_FOUND

        def post(self, id):

            try:
                int(id) == id
                int(id) > 0
                if CostCenterEntity.find_center(id):

                    return const.GENERAL_ID_ALREADY_EXISTS
                data = request.get_json()
                center = CostCenterEntity(**data)
                if CostCenterEntity.find_center_department(center.department_name):
                    return const.COST_CENTER_DEPARTMENT_ALREADY_EXISTS
                center.id = id
                center.save_center()
                return center.json(), 200
            except ValueError:
                return const.GENERAL_ID_NOT_FOUND
            except:

                return const.GENERAL_INTERNAL_ERROR_SAVE

        def put(self, id):

            try:
                int(id) == id
                data = request.get_json()
                center = CostCenterEntity.find_center(id)
                if center:
                    center.update_center(**data)
                    center.save_center()
                    return center.json(), 200
                return const.GENERAL_ID_NOT_FOUND
            except ValueError:
                return const.GENERAL_ID_NOT_FOUND
            except:

                return const.GENERAL_INTERNAL_ERROR_SAVE

        def delete(self, id):

            try:
                int(id) == id
                center = CostCenterEntity.find_center(id)
                if center:
                    center.delete_center()
                    return const.GENERAL_ID_DELETED
                return const.GENERAL_ID_NOT_FOUND
            except ValueError:
                return const.GENERAL_ID_NOT_FOUND
            except:
                return const.GENERAL_INTERNAL_ERROR_DELETE

    class ProjectsUsers(Resource):

        def get(self):
            return {'Projects Users': [project_user.json() for project_user in ProjectUserEntity.query.all()]}, 200

    class ProjectsIDUsers(Resource):

        def get(self, id_project):
            try:
                int(id_project) == id_project
                project_user = ProjectUserEntity.find_project_all_users(
                    id_project)
                list_users = [item.user_id for item in project_user]
                dict_users = {}
                contador = 1
                for id_user in list_users:
                    name = UsersEntity.find_user(id_user)
                    dict_users['user ' + str(contador)] = name.json()
                    contador += 1
                return {f'USERS FROM PROJECT ID {id_project}': dict_users}, 200
            except ValueError:
                return const.GENERAL_ID_NOT_FOUND
            except:
                return const.GENERAL_ID_NOT_FOUND

        def post(self, id_project):
            try:
                int(id_project) == id_project
                data = request.get_json()
                project_user = ProjectUserEntity(**data)
                project_user.project_id = id_project
                project_user.save_project_user()
                return project_user.json(), 200
            except ValueError:
                return const.GENERAL_ID_NOT_FOUND
            except:

                return const.GENERAL_INTERNAL_ERROR_SAVE

        def delete(self, id_project, id_user):

            try:
                int(id_project) == id_project
                int(id_user) == id_user
                if int(id_project) <= 0:
                    return const.PROJECT_NOT_FOUND
                elif int(id_user) <= 0:
                    return const.USER_NOT_FOUND
                project_user = ProjectUserEntity.find_project_by_user(
                    id_project, id_user)
                if project_user:
                    project_user.delete_project_user()
                    return const.GENERAL_ID_DELETED
                return const.GENERAL_ID_NOT_FOUND
            except ValueError:
                try:
                    int(id_project) == id_project
                    return const.USER_NOT_FOUND
                except:
                    return const.PROJECT_NOT_FOUND
            except:
                return const.GENERAL_INTERNAL_ERROR_DELETE


# ENDPOINTS:
    api = Api(app)
    # api.add_resource(IndexEntity, '/index', '/index/')
    api.add_resource(Projects, '/projects', '/projects/')
    api.add_resource(Project, '/projects/<id>', '/projects/<id>/')
    api.add_resource(Users, '/users', '/users/')
    api.add_resource(User, '/users/<id>', '/users/<id>/')
    api.add_resource(Centers, '/costcenters', '/costcenters/')
    api.add_resource(Center, '/costcenters/<id>', '/costcenters/<id>/')
    api.add_resource(ProjectsUsers, '/projects/users', '/projects/users/')
    api.add_resource(ProjectsIDUsers, '/projects/<id_project>/users',
                     '/projects/<id_project>/users/', '/projects/<id_project>/users/<id_user>', '/projects/<id_project>/users/<id_user>/')

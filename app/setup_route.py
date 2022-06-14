from flask import request
from flask_restful import Resource, Api
from app.entity import ProjectEntity, UsersEntity, CostCenterEntity
from app.errors import error_id_not_int



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
			# MODIFICADO
			error_id_not_int(id)
			# MODIFICADO
			project = ProjectEntity.find_project(id)
			if project:
				return project.json()
			return {'message': 'Project not found.'}, 404

		def get(self, id):
			#error_id_not_int(id)
			try:
				int(id) == id
				project = ProjectEntity.find_project(id)
				if project:
					return project.json()
				return {'message': 'Project not found.'}, 404

			except ValueError:
				return {'message': f'Oops! This ID {id} is not valid'}, 400


		def post(self, id):
			#error_id_not_int(id)
			try:
				int(id) == id
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
			#error_id_not_int(id)
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
			#error_id_not_int(id)
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
			#error_id_not_int(id)
			try:
				int(id) == id
				user = UsersEntity.find_user(id)

				if user:
					return user.json()
				return {'message': 'User not found.'}, 404

			except ValueError:
				return {'message': f'Oops! This User ID {id} is not valid'}, 400


		def post(self, id):
			#error_id_not_int(id)
			try:
				int(id) == id
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
			#error_id_not_int(id)
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
			#error_id_not_int(id)
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
			data = request.get_json()
			center = CostCenterEntity(**data)
			try:
				center.save_center()
			except:
				# Internal Server Error
				return {'message': 'An internal error occurred trying to save cost center.'}, 500
			return center.json()

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


		def get(self, id):
			# MODIFICADO
			try:
				int(id) == id
			except ValueError:
				return {'message': f'Oops! This ID {id} is not valid'}, 400
			# MODIFICADO
			center = CostCenterEntity.find_center(id)
			if center:
				return center.json()
			return {'message': 'Cost Center not found.'}, 404

		def get(self, id):
			#error_id_not_int(id)
			try:
				int(id) == id
				center = CostCenterEntity.find_center(id)

				if center:
					return center.json()
				return {'message': 'Cost Center not found.'}, 404

			except ValueError:
				return {'message': f'Oops! This Cost Center ID {id} is not valid'}, 400


		def post(self, id):
			#error_id_not_int(id)
			try:
				int(id) == id

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
			#error_id_not_int(id)
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
			#rror_id_not_int(id)
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

				
	# ENDPOINTS:			
	api = Api(app)

	api.add_resource(IndexEntity, '/index' )
	api.add_resource(Projects, '/projects')
	api.add_resource(Project, '/projects/<id>')
	api.add_resource(Users, '/users')
	api.add_resource(User, '/users/<id>')
	api.add_resource(Centers, '/costcenters')
	api.add_resource(Center, '/costcenters/<id>')

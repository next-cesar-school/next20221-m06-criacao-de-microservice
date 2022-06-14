
def error_id_not_int(id):
    try:
        int(id) == id
    except ValueError:
        return {'message': f'Oops! This ID {id} is not valid'}, 400
        

# def error_check():


# 	# value error
# 	try:
# 		int(id) == id
# 	except ValueError:
# 		return {'message':f'Oops! This ID {id} is not valid'}, 400

# @classmethod
# def find_user(cls, id):
# 	# igual a SELECT * FROM users WHERE id(do db) = id(do parametro)
# 		user = cls.query.filter_by(id=id).first()
# 		if user:
# 			return user
# 		return None



def classmethods():

	@classmethod
	def find_id(cls, id):
		# SELECT * FROM projects WHERE id(do db) = id(do parametro)
		id_find = cls.query.filter_by(id=id).first()
		if id_find:
			return id_find
		return None
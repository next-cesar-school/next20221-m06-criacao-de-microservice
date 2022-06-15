@classmethod
def query_by_id(cls, id):
	# SELECT * FROM projects WHERE id(do db) = id(do parametro)
	query = cls.query.filter_by(id=id).first()
	if query:
		return query
	return None
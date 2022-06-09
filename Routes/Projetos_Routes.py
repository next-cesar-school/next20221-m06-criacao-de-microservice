from flask import request, flash, url_for, redirect, render_template
# from CRUD_PROJETOS_CESAR import app, db
# from Models import Projeto_Entity



def setup_route(app):
	# Função visão geral.
	@app.route('/index')
	def index():
		return "E aí, essa galera?"
	# return render_template('show_projetos.html', projeto=Projeto_Entity.query.order_by(Projeto_Entity.id).all())

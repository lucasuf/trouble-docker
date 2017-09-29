from flask import Blueprint
from flask import request, render_template
from project.models import *

incidentes = Blueprint('incidentes', __name__,template_folder='templates')

@incidentes.route('/')
def index():
	return render_template('index_incidentes.html')

@incidentes.route('/cadastrar/')
def cadastrar():
	return render_template('cadastrar.html')

@incidentes.route('/editar/')
def editar():
	return 'Incidentes editar'

@incidentes.route('/visualizar/')
def visualizar():
	return render_template('visualizar_todos.html')
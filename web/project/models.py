# models.py

import datetime
from project.app import db


class Bilhete(db.Model):
	__tablename__='bilhete'

	id = db.Column(db.Integer, primary_key=True)
	num_bilhete = db.Column(db.String(10))
	date_posted = db.Column(db.DateTime, nullable=False)
	parecer = db.relationship('Parecer',uselist=False, backref='bilhete',
		lazy='dynamic')

	def __init__(self, num_bilhete=None, date_posted=None):
		self.num_bilhete = num_bilhete
		self.date_posted = datetime.datetime.now()

class Parecer(db.Model):
	__tablename__='parecer'

	id = db.Column(db.Integer, primary_key=True)
	fiscalCampo = db.Column(db.String(50))
	bilhete_id = db.Column(db.Integer, db.ForeignKey('bilhete.id'))

	def __init__(self, fiscalCampo=None, bilhete_id=None):
		self.fiscalCampo = fiscalCampo
		self.bilhete_id = bilhete_id


# UM - PARA - MUITOS
# Contrato ----> Bilhete
# Contrato ----> Itens
# Contrato ----> Aditivo
# Aditivo ----> Itens
# Bilhete ----> Itens



# UM - PARA - UM
# Bilhete ----> Parecer
# Bilhete ----> Local
# Bilhete ----> Informação Serviço
# Bilhete ----> Atendimento
# -----------------------------------------------------------------------------------
	





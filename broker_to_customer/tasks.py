from __future__ import absolute_import
from domain_specific_language.celery import app

@app.task
def broadcast_brokers(requirement_id):
	print 'called broadcast brokers', requirement_id
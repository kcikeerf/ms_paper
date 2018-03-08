from pymongo import MongoClient

db_mongo = MongoClient(
	host='localhost',
	port=27017,
	document_class=dict,
	tz_aware=False,
	connect=True
)

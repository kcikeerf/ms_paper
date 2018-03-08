from elasticsearch import Elasticsearch

db_es = Elasticsearch(
	['localhost'],
	port=9200) 
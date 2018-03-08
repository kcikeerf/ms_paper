# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request, abort
from bson import json_util, ObjectId
import json

from db.mongodb import db_mongo
from db.elastic_search import db_es
from resources.custom_errors import InvalidParameter

quizs = Blueprint('quizs', __name__)

QUIZ_MODEL_ATTRIBUTES = [ 
	"_id",
	"node_uid",
	"pap_uid",
	"tbs_uid",
	"tpl_id",
	"ext1",
	"ext2",
	"cat",
	"type",
	"text",
	"answer",
	"desc",
	"score",
	"time",
	"levelword2",
	"level",
	"levelword",
	"levelorder",
	"order",
	"dt_update",
	"dt_add",
	"bank_paper_pap_ids",
	"is_II_quiz",
	"is_empty"
]

# 获取单题列表
@quizs.route('/list', methods=['GET'])
def list():
	resp =[]
	results = db_mongo.swtk_production["mongodb_bank_tests"].find({})
	for item in results:
		try:
			resp.append(item)
		except Exception as e:
			print e
	return json.dumps(resp, default=json_util.default)

# 创建单题
@quizs.route('/', methods=['POST'])
def create():
	data = request.json
	new_value = {}
	for item in data.items():
		if item[0] in QUIZ_MODEL_ATTRIBUTES:
			new_value[item[0]] = item[1]
	if not new_value:
		# raise InvalidParameter(u"空的") 
		raise InvalidParameter() 
	else:
		pass
	result = db_mongo.swtk_production["mongodb_bank_tests"].insert_one(new_value)
	print(result.inserted_id)
	return json.dumps({"msg": "success!", "data": str(result.inserted_id) })

# 删除单题
@quizs.route('/<_id>', methods=['DELETE'])
def remove(_id):
	result = db_mongo.swtk_production["mongodb_bank_tests"].delete_many({"_id": ObjectId(_id)})
	return json.dumps({"msg": "success!","data": result.deleted_count})

# 更新单题
@quizs.route('/<_id>', methods=['PUT'])
def update(_id):
	data = request.json
	modified_value = {}
	for item in data.items():
		if item[0] in QUIZ_MODEL_ATTRIBUTES:
			modified_value[item[0]] = item[1]
	if not modified_value:
		# raise InvalidParameter(u"空的") 
		raise InvalidParameter() 
	else:
		pass
	result = db_mongo.swtk_production["mongodb_bank_tests"].update_one({"_id": ObjectId(_id)}, { "$set": modified_value})
	return json.dumps({"msg": "success!","data": ""})

# 查看单题
@quizs.route('/<_id>', methods=['GET'])
def detail(_id):
	resp =[]
	result = db_mongo.swtk_production["mongodb_bank_tests"].find_one({"_id": ObjectId(_id)})
	return json.dumps(result, default=json_util.default)

# 查看单题
@quizs.route('/find_similar', methods=['POST'])
def es_find_similar():
	_data = request.json
	res = db_es.search(index="zx2",body=_data)
	return json.dumps(res, default=json_util.default, ensure_ascii=False).encode('utf8')

# # 获取单题列表
# @quizs.route('/es/list', methods=['GET'])
# def es_list():
# 	resp =[]
# 	results = db_mongo.swtk_production["mongodb_bank_tests"].find({})
# 	for item in results:
# 		try:
# 			resp.append(item)
# 		except Exception as e:
# 			print e
# 	return json.dumps(resp, default=json_util.default)

# # 创建单题
# @quizs.route('/es/', methods=['POST'])
# def es_create():
# 	data = request.json
# 	new_value = {}
# 	for item in data.items():
# 		if item[0] in QUIZ_MODEL_ATTRIBUTES:
# 			new_value[item[0]] = item[1]
# 	if not new_value:
# 		# raise InvalidParameter(u"空的") 
# 		raise InvalidParameter() 
# 	else:
# 		pass
# 	result = db_mongo.swtk_production["mongodb_bank_tests"].insert_one(new_value)
# 	print(result.inserted_id)
# 	return json.dumps({"msg": "success!", "data": str(result.inserted_id) })

# # 删除单题
# @quizs.route('/es/<_id>', methods=['DELETE'])
# def es_remove(_id):
# 	result = db_mongo.swtk_production["mongodb_bank_tests"].delete_many({"_id": ObjectId(_id)})
# 	return json.dumps({"msg": "success!","data": result.deleted_count})

# # 更新单题
# @quizs.route('/es/<_id>', methods=['PUT'])
# def es_update(_id):
# 	data = request.json
# 	modified_value = {}
# 	for item in data.items():
# 		if item[0] in QUIZ_MODEL_ATTRIBUTES:
# 			modified_value[item[0]] = item[1]
# 	if not modified_value:
# 		# raise InvalidParameter(u"空的") 
# 		raise InvalidParameter() 
# 	else:
# 		pass
# 	result = db_mongo.swtk_production["mongodb_bank_tests"].update_one({"_id": ObjectId(_id)}, { "$set": modified_value})
# 	return json.dumps({"msg": "success!","data": ""})

# # 查看单题
# @quizs.route('/<_id>', methods=['GET'])
# def es_detail(_id):
# 	resp =[]
# 	result = db_mongo.swtk_production["mongodb_bank_tests"].find_one({"_id": ObjectId(_id)})
# 	return json.dumps(result, default=json_util.default)


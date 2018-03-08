# -*- coding: utf-8 -*-

from flask import Flask
from resources.quizs import quizs
from  resources.custom_errors import InvalidParameter
import json

app = Flask(__name__)
app.register_blueprint(quizs,url_prefix="/quizs")

@app.errorhandler(InvalidParameter)
def invalid_parameter(error):
    print(error.message)
    return json.dumps({"msg": "invalid parameters!"}, ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True)
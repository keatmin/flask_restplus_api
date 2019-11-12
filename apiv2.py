from flask import Blueprint
from flask_restplus import Api
from apis.foodAI import api as foodai_api

blueprint = Blueprint('foodai', __name__)
api = Api(blueprint, 
title='Naluri Machine Learning API', 
version='2.0',
description='Predictors for conversation change and sustain')

api.add_namespace(foodai_api)


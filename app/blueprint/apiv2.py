from flask import Blueprint
from flask_restplus import Api
from ..apis.foodAI import api as foodai_api

blueprint = Blueprint("foodai", __name__)
api = Api(
    blueprint,
    title="Machine Learning API",
    version="2.0",
    description="ML/AI predictors for food images and NLP",
)
api.add_namespace(foodai_api)

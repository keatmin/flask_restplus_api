from flask import request, Flask
from flask_restplus import Api
from apiv2 import blueprint as api_v2

app = Flask(__name__)
api = Api(app)
app.register_blueprint(api_v2, url_prefix='/foodai/2')
app.run(debug=True)


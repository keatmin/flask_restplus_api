from flask_restplus import Namespace, Resource, fields

api = Namespace('foodai', description='Food image recognition engine')


@api.route('/')
class HelloWorld(Resource): 
    @api.doc('Front-end interface for public to test model')
    def get(self): 
        """
        UI interface for testing
        """
        return "Hello World!"

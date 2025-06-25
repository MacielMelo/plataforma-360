from flask import jsonify

def init_routes(app):
    @app.route("/", methods=['GET'])
    def hello_world():
        return jsonify({"message": "Hello, World!"})
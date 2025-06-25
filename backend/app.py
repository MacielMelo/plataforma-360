from flask import Flask
from controllers.hello_world_controller import init_routes

app = Flask(__name__)
init_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
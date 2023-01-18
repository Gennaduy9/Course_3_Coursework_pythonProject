from flask import Flask, send_from_directory
from appi.main.views import main_blueprint
from appi.api.views import api_blueprint


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

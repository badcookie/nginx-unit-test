from flask import Flask

flask_app = Flask(__name__)


@flask_app.route('/', methods=['GET'])
def get_request():
    return 'Success'


from flask import Flask

application = Flask(__name__)


@application.route('/', methods=['GET'])
def get_request():
    return 'Success\n'


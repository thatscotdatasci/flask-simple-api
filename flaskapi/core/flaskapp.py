import os
import logging
import datetime

from flask import Flask, request, jsonify

from flaskapi.models.user import User
from flaskapi.models import utils as model_utils
from flaskapi.helpers.database import Database
from flaskapi.helpers.exceptions import MissingArguments

application = Flask(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    application.logger.handlers = gunicorn_logger.handlers
    application.logger.setLevel(gunicorn_logger.level)

project_dir = os.path.dirname(os.path.abspath(__file__))
database_name = 'flaskapi.sqlite'
database_file = f'sqlite:///{os.path.join(project_dir, database_name)}'
database = Database(database_file, application)


def main():
    application.run(debug=True, host='0.0.0.0', port=8080)
    application.logger.info('Initialising flask-api...')


@application.route('/user', methods=['POST'])
def user_post():
    req_data = request.get_json()

    if not req_data or not {'first_name', 'surname'}.issubset(req_data.keys()):
        application.logger.error('Missing required argument(s)')
        raise MissingArguments('Missing required argument(s)')

    first_name = req_data['first_name']
    surname = req_data['surname']

    user = User(
        first_name=first_name,
        surname=surname,
        added=datetime.datetime.now(),
        edited=datetime.datetime.now()
    )

    application.logger.debug('Adding new user to db')
    database.db_session.add(user)
    database.db_session.commit()
    application.logger.debug(f'New user {user.id} added successfully')
    return jsonify({"id": user.id})


@application.route('/user/<int:user_id>', methods=['GET'])
def user_get(user_id):
    application.logger.debug(f'Attempting to get user with ID: {user_id}')
    user = database.db_session.query(User).filter_by(id=user_id).first()
    if user:
        application.logger.debug(f'Serving user information')
        return jsonify(model_utils.to_dict(user))
    return jsonify({})


@application.errorhandler(MissingArguments)
def handle_missing_arguments(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@application.teardown_appcontext
def shutdown_session(exception=None):
    database.db_session.remove()


if __name__ == "__main__":
    main()

import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='flaskapi: Simple API written in Flask to test various AWS features')
    parser.add_argument('--flaskapi-log', help='Path to a json file containing the logging configuration', default='logging.json', dest='log_conf')
    parser.add_argument('--flaskapi-database', help='Path to a file containing the database connection string', default='flaskapi-mysql-rds.secret', dest='db_string')
    args, unknown_args = parser.parse_known_args()
    return args

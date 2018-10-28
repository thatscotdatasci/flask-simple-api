import json

name = 'flaskapi'
workers = 4
bind = '0.0.0.0:8080'
logconfig_dict = json.load(open('logging.json'))

#!/usr/bin/python3
'''Doc for status'''
from api.v1.views import app_views


@app_views.route('/status')
def status():
    '''Doc for status'''
    return {"status": "OK"}

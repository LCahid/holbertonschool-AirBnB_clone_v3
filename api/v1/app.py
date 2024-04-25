from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
'''Doc for api'''
app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def final(self):
    '''Doc for teardown'''
    storage.close()


if __name__ == "__main__":
    HBNB_API_HOST = getenv('HBNB_API_HOST', default='0.0.0.0')
    HBNB_API_PORT = getenv('HBNB_API_PORT', default=5000)
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)

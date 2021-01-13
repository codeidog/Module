from flask import Flask
from  SubModule import submodule
import json
import logging
version = '1.0.1.2'
app = Flask(__name__)
app.register_blueprint(submodule, url_prefix='/submodule')

@app.route('/')
def index():
    global version
    returnDict = {
        'name' : __name__,
        'version': version
    }
    return json.dumps(returnDict, indent=4, sort_keys=True )

if __name__ == "__main__":

    app.run()

#Producton use by gunicorn
if __name__ != '__main__':    
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
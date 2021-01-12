from flask import Flask
from  SubModule import submodule
import json
version = '1.0.6'
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
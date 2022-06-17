from flask import Flask
from master.config_db import setup_db, db
from master.config_general import setup_general_config
from master.setup_route import setup_route

app = Flask(__name__)


@app.before_first_request
def init_db():
    db.create_all()

setup_general_config(app)
setup_db(app)
setup_route(app)


if __name__ == '__main__':
    app.run(debug=True)

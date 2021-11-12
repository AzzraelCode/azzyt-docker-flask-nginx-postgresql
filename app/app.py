from flask import Flask


import routes
from cli import bp
from db import conn

app = Flask(__name__)

app.config.from_pyfile("config.py")
app.config['JSON_AS_ASCII'] = False # для кириллицы в конфиге
conn.init_app(app)

app.register_blueprint(bp)
app.register_blueprint(routes.bp)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
from flask import jsonify, current_app
from flask import Blueprint
from sqlalchemy import func

from models.Names import Names

bp = Blueprint('routes', __name__)

@bp.route("/")
def index():
    return  jsonify([
        {"response": current_app.config['HELLO_MESSAGE']},
        {"db_path": current_app.config['SQLALCHEMY_DATABASE_URI']}
    ])

@bp.route("/name")
def name():
    n = Names.query.order_by(func.random()).first()
    return jsonify({"names" : "%s = %d" % (n.name, n.amount) })

@bp.route("/add_random")
def add_random():
    n = Names()
    n.fill_random()
    n.save()
    return jsonify({"added" : "%s = %d" % (n.name, n.amount)})
from flask import Blueprint

items_blueprint=Blueprint("items_blueprint",__name__,url_prefix='/api')

@items_blueprint.route('/hello')
def hello():
    return "hello"
@items_blueprint.route('/hello', methods=["POST"])
def postdone():
    return "POST done"
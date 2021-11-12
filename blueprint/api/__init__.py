from flask import Blueprint
# from blueprint.api.items import items_blueprint
# from blueprint.api.user import user_blueprint


api_blueprint=Blueprint("api_blueprint",__name__,url_prefix='/api')
# api_blueprint.register_blueprint(user_blueprint)
# api_blueprint.register_blueprint(items_blueprint)

@api_blueprint.route('/bye')
def bye():
    return 'bye'
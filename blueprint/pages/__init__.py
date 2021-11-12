from flask import Blueprint,render_template
from blueprint.pages.other import other_blueprint
from blueprint.pages.main import main_blueprint
pages_blueprint=Blueprint("pages_blueprint",__name__)
pages_blueprint.register_blueprint(other_blueprint)
pages_blueprint.register_blueprint(main_blueprint)

@pages_blueprint.route('/4')
def d():
    return render_template('contact.html')

@pages_blueprint.route('/5')
def c():
    return render_template('single.html')
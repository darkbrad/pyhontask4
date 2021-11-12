from flask import Blueprint,render_template
main_blueprint=Blueprint("main_blueprint",__name__)
@main_blueprint.route('/3')
def b():
    return render_template('index.html')

@main_blueprint.route('/1')
def a():
    return render_template('single-works.html')
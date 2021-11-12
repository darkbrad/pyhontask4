from flask import Blueprint,render_template
other_blueprint=Blueprint("other_blueprint",__name__)


@other_blueprint.route('/')
def f():
    return render_template('works.html')

@other_blueprint.route('/2')
def e():
    return render_template('name.html')
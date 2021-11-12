from flask import Blueprint,request,jsonify
from pydantic import BaseModel
import pydantic
from typing import Optional
user_blueprint=Blueprint("user_blueprint",__name__,url_prefix='/api')
class NewUserModel(BaseModel):
    login: str
    password: str
    items: Optional[list]

@user_blueprint.route('/',methods=["POST"])
def post11():
    try:
        data = NewUserModel(**request.json)
    except pydantic.error_wrappers.ValidationError:
        return jsonify({"info": "Invalid data format"}, )
    else:
        return "done"


@user_blueprint.route('/')
def get():
    return "GET"

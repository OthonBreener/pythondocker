from flask import Flask, request
from flask_pydantic_spec import FlaskPydanticSpec, Request, Response

from app.ext import UserRepository

app = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='Api estudos 2')
spec.register(app)

@app.route("/", methods=["GET"])
def hello_world():
    """
    Rota Hellow
    """
    return "Olá pessoas!"

@app.route("/insert", methods=["POST"])
def insert_new_user():

    user = UserRepository()
    params = request.json
    user.insert_user(params['name'])

    return "Novo usuário inserido com sucesso!", 200

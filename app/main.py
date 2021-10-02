from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec, Request, Response

app = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='Api estudos 2')
spec.register(app)

@app.route("/", methods=["GET"])
def hello_world():
    """
    Rota Hellow
    """
    return "Olá pessoas!"

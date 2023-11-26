from flask import Flask, request, Response
from src.genie import Genie
from src.file_loader import load_pdf
import os


app = Flask(__name__)

load_pdf("assets/owners_manual.pdf")
genie = Genie("result.txt")


@app.route("/")
def hello_world():
    return "Hello AI enjoyer!"


@app.route("/query/<query_input>")
def query(query_input):
    api_key = request.headers.get("api")
    if api_key == None or api_key != os.environ["APP_KEY"]:
        return Response("Unauthorized", status=401)

    return genie.ask(query_input)

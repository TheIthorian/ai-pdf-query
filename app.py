from flask import Flask, request, Response
from src.genie import Genie
from src.file_loader import load_pdf
import os


app = Flask(__name__)

load_pdf("assets/Warhammer_Fantasy_Roleplay_PDF_version4.pdf")
genie = Genie("result.txt")


@app.route("/")
def hello_world():
    return "Hello AI enjoyer!"


@app.route("/query/<query_input>")
def query(query_input):
    api_key = request.headers.get("api")
    if api_key == None or api_key != os.environ["APP_KEY"]:
        return Response("Unauthorized", status=401)

    try:
        return genie.ask(query_input) or "no answer"
    except Exception as e:
        print(e)
        return Response(
            "Error generating response. Please try again later.", status=500
        )

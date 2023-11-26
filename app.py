from flask import Flask
from src.genie import Genie
from src.file_loader import load_pdf
import os


app = Flask(__name__)

load_pdf("assets/owners_manual.pdf")
genie = Genie("result.txt")


@app.route("/")
def hello_world():
    return "Hello, Docker!"


@app.route("/query/<query_input>")
def query(query_input):
    return genie.ask(query_input)

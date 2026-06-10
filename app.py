from flask import Flask, render_templates

app = flask(__name__)


@app.route("/")
def welcome():
  print("hello")

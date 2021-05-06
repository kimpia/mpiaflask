from flask import Blueprint

blog = Blueprint("blog", __name__)

@blog.route("/")
def index():
    return "<h1>Hello World</h1>"
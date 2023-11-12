from flask import Blueprint


zhulik = Blueprint(
    "zhulik", __name__)


def page():
    return "Hello, zhulik!"


zhulik.add_url_rule(
    "/zhulik/page", view_func=page)


def get_blueprints():
    return [zhulik]

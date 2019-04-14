#-*- coding:utf-8 -*-

from flask import Flask,g,request
from viewhandler.page_blueprint import page

app = Flask(__name__)

app.config.from_pyfile('config.py')

BLUEPRINT = [page]

def bootstrap_app(app):
    for view in BLUEPRINT:
        app.register_blueprint(view)

    @app.before_request
    def before():
        args = {k:v[0] for k,v in dict(request.args).items()} #get
        args_form = {k:v[0] for k,v in dict(request.form).items()}#post
        args.update(args_form)
        g.args = args

bootstrap_app(app)

if __name__ == '__main__':
    app.run(host=app.config['WEB_HOST'],port = app.config['WEB_PORT'])
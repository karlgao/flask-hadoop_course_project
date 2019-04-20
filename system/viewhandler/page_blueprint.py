#-*- coding:utf-8 -*-

from flask import Blueprint,jsonify,g,render_template


page = Blueprint('page',__name__,url_prefix='/page')

@page.route('/index')

def index():
    print (g.args.get('account',None))
    return jsonify({'adsadfa':123123})

@page.route('/main/')
def main():
    return render_template('main.html')
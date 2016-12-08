import datetime
from flask import Flask, request, render_template, \
    redirect, url_for, request, session, flash, g
from functools import wraps
from model import *
from app import app


@app.before_request
def before_request():
    initialize_db()


@app.route('/')
def manager():
    filial = request.args.get('filial')
    return render_template('manager.html',
                           orders=list(Order.select().where(Order.filial == filial).order_by(Order.id.desc())))


@app.route('/monitor')
def monitor():
    filial = request.args.get('filial')
    return render_template('monitor.html',
                           orders=list(Order.select().where(Order.filial == filial).order_by(Order.id.desc()).limit(8)))

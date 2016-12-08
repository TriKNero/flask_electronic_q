import datetime
from flask import Flask, request, render_template, \
    redirect, url_for, request, session, flash, g
from functools import wraps
import sqlite3
from model import *
from app import app


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))

    return wrap


@app.route('/'+request.form['username'])
@login_required
def home():
    return render_template('queue.html', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['password'] != 'admin':
            error = 'invalid login. Please try again'
        else:
            session['logged_in'] = True
            flash('You login in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('login'))

import datetime
import uuid
from flask import Flask,render_template,url_for,request,redirect,jsonify,session
from flask_sessionstore import Session
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from sqlalchemy.engine import Engine
from sqlalchemy import event,create_engine,or_,desc
from flask_login import UserMixin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app=Flask(__name__)
app.config['SECRET_KEY']='secrettttttttt'
app.config['WTF_CSRF_SECRET_KEY']='wtffdjfk'
db = SQLAlchemy(app)
csrf=CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///combs.db'
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY_TABLE'] = 'sessions'
app.config['SESSION_SQLALCHEMY'] = db
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if type(dbapi_connection) is sqlite3.Connection:  
       cursor = dbapi_connection.cursor()
       cursor.execute("PRAGMA foreign_keys=ON")
       cursor.close()

admin=Admin(app,name='My App',template_mode='bootstrap3')
engine=create_engine('sqlite:///combs.db')
Session(app)





if __name__=='__main__':
    app.run(debug='True')

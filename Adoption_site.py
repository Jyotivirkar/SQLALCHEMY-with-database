From flask os
From flask import Flask render_template, url_for, redirect
from flask_Sqlalchemy import sqlalchemy
From flask_migrate import migrate

app=Flask(__name__) 

app. Config['secret_key']='mysecretkey'

Basedir=OS.path.absname(os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'os.path.join(basedir, 'data_sqlite'
app. Config['SQLALCHEMY_TRACK_MODIFICATIONS']= false
 
db=SQLALCHEMY(app) 
Migrate(app,Db) 

Class puppy (db.model) :
    
   _tablename_='puppies'

   id=db.column(db.integer,primary key=true) 
   Name=db.column(db.text) 


  def __init__(self, name):
     self. Name=name
 
  def __repr__(self):
     return f"puppy name is {self. Name}"
  

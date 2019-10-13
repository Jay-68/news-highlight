from flask import render_template
from app import main

# app views
@main.route('/')
def index():
  '''
  view root page that returns the index page and its data
  '''
  return render_template('index.html')
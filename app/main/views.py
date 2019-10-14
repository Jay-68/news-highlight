from flask import render_template, request, redirect, url_for
# import sys
from . import main
from ..request import get_sources, get_articles
from ..models import Sources

# app views
@main.route('/')
def index():
    '''
    view root page that returns the index page and its data
    '''
    articles = get_articles()
    title = 'News Highlights'


    return render_template('index.html', title=title,articles=articles)


@main.route('/sources/<id>')
def articles():
    '''
    routing to article pages
    '''
    articles = get_articles()
    title = 'Latest articles'

    return render_template('articles.html', title=title, articles=articles)

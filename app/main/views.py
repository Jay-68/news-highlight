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
    entertainment = get_sources('entertainment')
    technology = get_sources('technology')
    business = get_sources('business')
    sports = get_sources('sports')
    print(entertainment[0].name)
    # title = get_sources('News Highlights')


    return render_template('index.html', entertainment=entertainment, technology=technology, business=business, sports=sports)


@main.route('/sources/<id>')
def articles(id):
    '''
    routing to article pages
    '''
    articles = get_articles(id)
    title = 'Latest articles'

    return render_template('articles.html', title=title, articles=articles)

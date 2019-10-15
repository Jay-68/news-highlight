from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_sources, get_articles
from ..models import Sources

# app views
@main.route('/')
def index():
    '''
    view root page that returns the index page and its data
    '''
    sources = get_sources()
    title = 'News Highlights'

    return render_template('index.html', title=title, sources=sources)


@main.route('/sources')
def articles():
    '''
    routing to article pages
    '''
    articles = get_articles()
    # print(articles)
    title = 'Latest articles'

    return render_template('articles.html', title=title, articles=articles)

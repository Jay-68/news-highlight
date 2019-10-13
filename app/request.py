import urllib.request
import json
from .models import Sources, Articles
from datetime import datetime

api_key = None
base_url = None
Articles_url = None


def configure_request(app):
    global api_key, base_url, base_url_articles
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    base_url_articles = app.config['ARTICLES_BASE_URL']

    print(api_key)
    print(base_url)


def get_sources(category):
    '''
    Function to get the json response to the provided url request
    '''
    get_sources_url = base_url.format(category, api_key)
    print(get_sources_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        sources_results = None
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
    return sources_results


def process_sources(sources_list):
    '''
    This function processes the news sources and returns a list of objects
    Args:
      sources_list: A list of dictionaries that contain the sources details
    '''
    sources_results = []

    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        sources_object = Sources(id, name, description, url, category, country)
        sources_results.append(sources_object)

    return sources_results

def get_articles(id):
  '''
  function provides json response to the request
  '''
  get_articles_url=base_url_articles.format(id,api_key)

  with urllib.request.urlopen(get_articles_url) as url:
    get_articles_data=url.read()
    get_articles_response=json.loads(get_articles_data)

    articles_results=None

    if get_articles_response['articles']:
      articles_results_list=
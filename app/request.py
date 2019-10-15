import urllib.request
import json
from config import Config
# import json
from .models import Sources, Articles
from datetime import datetime

api_key = None

base_url = None
Articles_url = None
api_key = Config.NEWS_API_KEY
base_url = Config.NEWS_SOURCES_BASE_URL
base_url_articles = Config.ARTICLES_BASE_URL
get_sources_url = base_url.format(base_url, api_key)
# print(api_key)
# print(base_url)


def get_sources():
    '''
    Function to get the json response to the provided url request
    '''

    with urllib.request.urlopen(base_url+api_key) as url:
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


def get_articles():
    '''
    function provides json response to the request
    '''
    # get_articles_url = base_url_articles.format()

    with urllib.request.urlopen(base_url_articles + api_key) as url:
        articles_results = json.loads(url.read())

        articles_object = None

        if articles_results['articles']:
            articles_object = process_articles(articles_results['articles'])

    return articles_object


def process_articles(articles_list):
    '''
    function that process request articles and returns the article object
    '''
    articles_object = []

    for article_item in articles_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')

        if image:
            articles_result = Articles(
                author, title, description, url, image, date)
            articles_object.append(articles_result)

    return articles_object

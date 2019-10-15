import os


class Config:
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?apiKey='
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey='
    NEW_API_KEY = os.environ.get('NEW_API_KEY')


class ProdConfig(Config):

    NEW_API_KEY = os.environ.get('NEW_API_KEY')
    DEBUG = False


class DevConfig(Config):
    DEBUG = True


Config_options = {
    'development': DevConfig,
    'production': ProdConfig
}

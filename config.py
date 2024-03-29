import os
# from dotenv import load_dotenv
# load_dotenv()

class Config:
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?apiKey='
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey='
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


Config_options = {
    'development': DevConfig,
    'production': ProdConfig
}

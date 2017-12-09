import os

class Config:
    '''
    main configuration class
    '''

    NEWS_API_KEY = '44b40f34d60a4884aff4338f6e05a4d3'
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources/{}?apiKey{}'

class ProdConfig(Config):
    '''
    Production configuration class that inherits from the main configurations class
    '''
    pass


class DevConfig(Config):
    '''
    Configuration class for development stage of the app
    '''
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
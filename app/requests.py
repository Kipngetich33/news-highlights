import urllib.request, json
from .models import News_Highlights, News_Highlights_by_source

#this part collects the API key
api_key = None

#this part collects the base url

def config_func(app):
    global base_url,api_key
    base_url = app.config['NEWS_API_BASE_URL']
    api_key =app.config['NEWS_API_KEY']

def get_source_names(search_keyword):
    '''
    This is a function that collects the news sources from the API
    '''
    configured_source_url1 = base_url.format(search_keyword,api_key)

    with urllib.request.urlopen(configured_source_url1) as url:
        collected_sources_data = url.read()
        source_names_json = json.loads(collected_sources_data)

        list_of_sources = None

        if source_names_json['sources']:
            successfully_collected_list =source_names_json['sources']
            list_of_sources= process_sources(successfully_collected_list)
    
    return list_of_sources

def get_articles(id):
    '''
    This is a function that retrives articles from a particular source based on the selected source
    '''
    configured_articles_url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=44b40f34d60a4884aff4338f6e05a4d3'
    with urllib.request.urlopen(configured_articles_url) as url:
        collected_articles_data = url.read()
        source_articles_json = json.loads(collected_articles_data)

        list_of_sources = None

        if source_articles_json['articles']:
            successfully_collected_articles =source_articles_json['articles']
            list_of_articles= process_articles(successfully_collected_articles)
    
    return list_of_articles  


def process_sources(source_response):
    '''
    A function that process json file results and defines them for the class
    '''
    populated_source_list =[]
    for source in source_response:
        source_name = source.get('name')
        source_id = source.get('id')
        source_url = source.get('url')
        source_description = source.get('description')
        source_object= News_Highlights(source_name,source_id,source_url,source_description)
        populated_source_list.append(source_object)

    return populated_source_list

def process_articles(articles_response):
    '''
    function that processes the json files of articles from the api key
    '''
    populated_articles_list = []
    for article in articles_response:
        article_name = article.get('author')
        article_description = article.get('description')
        article_time = article.get('time')
        article_objects = News_Highlights_by_source(article_name,article_description,article_time)
        populated_articles_list.append(article_objects)

    return populated_articles_list 






    




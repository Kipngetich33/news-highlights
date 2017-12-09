import urllib.request, json
from .models import News_Highlights

#this part collects the API key
api_key = None

#this part collects the base url

def config_func(app):
    global base_url,api_key
    base_url = app.config['NEWS_API_BASE_URL']
    api_key =app.config['NEWS_API_KEY']

def get_source_names(type_of_news):
    '''
    This is a function that collects the news sources from the API
    '''
    configured_source_url = 'https://newsapi.org/v2/sources?apiKey=44b40f34d60a4884aff4338f6e05a4d3'
    # base_url.format(type_of_news,api_key)

    with urllib.request.urlopen(configured_source_url) as url:
        collected_sources_data = url.read()
        source_names_json = json.loads(collected_sources_data)

        list_of_sources = None

        if source_names_json['sources']:
            successfully_collected_list =source_names_json['sources']
            list_of_sources= process_sources(successfully_collected_list)
    
    return list_of_sources

def process_sources(source_response):
    '''
    A function that process json file results and defines them for the class
    '''
    populated_source_list =[]
    for source in source_response:
        source_name = source.get('name')
        source_object= News_Highlights(source_name)
        populated_source_list.append(source_object)

    return populated_source_list





    




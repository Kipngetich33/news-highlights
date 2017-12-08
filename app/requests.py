import urllib.request , json
from models import News_Highlights

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
            successfully_collected_list =source_names_json
            processed_list= process_sources(successfully_collected_list)
    
    return processed_list

def process_sources():
    




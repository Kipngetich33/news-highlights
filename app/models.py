class News_Highlights:
    '''
    This is class that will determine the behaviour of the news clas
    '''
    def __init__(self,source_name,source_id,source_url,source_description):
        '''
        function instantiates the class sources 
        '''
        self.source_name = source_name
        self.source_id = source_id
        self.source_url = source_url
        self.source_description = source_description

class News_Highlights_by_source:
    '''
    This class instatitate highlight objects for each specific source
    '''
    def __init__(self,article_name,article_description,article_time,article_url,article_image,article_title):
        '''
        Class that instantiates objects of the news article objects of the news sources
        '''
        self.article_name = article_name
        self.article_description = article_description
        self.article_time = article_time
        self.article_url = article_url
        self.article_image = article_image
        self.article_title = article_title


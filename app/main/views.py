from flask import render_template ,request ,redirect ,url_for
from . import main
from ..requests import get_source_names

@main.route('/')
def index():
    '''
    Functiont that returns the index page and its data
    '''
    title = 'Trending News Base'

    #this part gets the different sources

    sources_and_name = get_source_names('sources')
    return render_template('index.html' title= title ,sources_and_name = sources_and_name)
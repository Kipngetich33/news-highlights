from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_source_names, get_articles

@main.route('/')
def index():
    '''
    Functiont that returns the index page and its data
    '''
    title = 'Trending News Base'

    sources_and_name = get_source_names('sources')
    return render_template('index.html', title= title ,sources_and_name = sources_and_name)


@main.route('/news_page/<source_id>')
def news_page(source_id):
    '''
    Function that returns the highlights page and its data
    '''
    title = 'Highlights'
    # this parts get different articles from a specified source

    source_and_articles = get_articles(source_id)
    return render_template('news_page.html', title = title, source_and_articles= source_and_articles )  
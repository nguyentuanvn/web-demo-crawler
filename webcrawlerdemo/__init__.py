from flask import Flask, request, render_template, redirect, url_for
from webcrawler.news import Article

app = Flask(__name__)

# Debug logging
import logging
import sys
# Defaults to stdout
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
try: 
    log.info('Logging to console')
except:
    _, ex, _ = sys.exc_info()
    log.error(ex.message)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/articles/show')
def show_article():
    url = request.args.get('url_to_clean')
    if not url:
        return redirect(url_for('index'))

    article = Article(url)
    a = {
        'title': article.title, 
        'date': article.date,
        'author': article.author,
        'related': article.related,
        'words_dict': article.words_dict,
        'top_image': article.top_image
    }
    return render_template('article/index.html', article=a, url=url)
    
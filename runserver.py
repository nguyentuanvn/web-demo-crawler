from webcrawlerdemo import app
from webcrawlerdemo.controllers import article

if __name__ == '__main__':
    app.register_blueprint(article.mod)
    app.run(debug=True)

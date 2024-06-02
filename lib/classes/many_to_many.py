class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
        if hasattr(author, '_articles'):
            author._articles.append(self)
        else:
            author._articles = [self]
        if hasattr(magazine, '_articles'):
            magazine._articles.append(self)
        else:
            magazine._articles = [self]

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title is immutable")


class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        Article(self, magazine, title)

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        return list(set(article.author for article in self._articles))

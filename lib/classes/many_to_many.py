class Article:
    all = []  # Class variable to keep track of all articles

    def __init__(self, author, magazine, title):
        # Validate title
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        
        self._title = title  # Use private attribute for title
        self.author = author  # The author of the article
        self.magazine = magazine  # The magazine the article is in
        
        # Add article to the author's list of articles
        author.add_article(self)
        # Add article to the magazine's list of articles
        magazine.add_article(self)

        Article.all.append(self)  # Add the article to the class-level list

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise Exception("Title cannot be changed after initialization")


    
class Author:
    all = []  # Class variable to keep track of all authors

    def __init__(self, name):
        # Validate name
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must have at least one character")
        
        self._name = name  # Use private attribute for name
        self._articles = []  # List to store articles written by this author
        self._magazines = []  # List to store magazines the author contributes to

        Author.all.append(self)  # Add the author to the class-level list

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise Exception("Author's name cannot be changed after initialization")

    def articles(self):
        return self._articles

    def magazines(self):
        return self._magazines  # Return list of magazines

    def add_article(self, article):
        # Add article to the author's articles list
        self._articles.append(article)
        # Add the magazine to the author's magazines list
        if article.magazine not in self._magazines:
            self._magazines.append(article.magazine)

    def topic_areas(self):
        # Return unique categories (topics) of magazines the author writes for
        return list(set(magazine.category for magazine in self._magazines))


class Magazine:
    all = []  # Class variable to keep track of all magazines

    def __init__(self, name, category):
        # Validate name length (between 2 and 16 characters)
        if len(name) < 2 or len(name) > 16:
            raise Exception("Magazine name must be between 2 and 16 characters")
        
        # Validate category
        if len(category) == 0:
            raise Exception("Category must have a length greater than 0")
        
        self._name = name  # Use private attribute for name
        self._category = category  # Use private attribute for category
        self._articles = []  # List to store articles in this magazine

        Magazine.all.append(self)  # Add the magazine to the class-level list

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 2 or len(value) > 16:
            raise Exception("Magazine name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if len(value) == 0:
            raise Exception("Category must have a length greater than 0")
        self._category = value

    def articles(self):
        return self._articles

    def add_article(self, article):
        # Add article to the magazine's articles list
        self._articles.append(article)

    @classmethod
    def top_publisher(cls):
        # Find the magazine with the most articles
        magazine_article_count = {}
        for article in Article.all:
            magazine_article_count[article.magazine] = magazine_article_count.get(article.magazine, 0) + 1
        return max(magazine_article_count, key=magazine_article_count.get)



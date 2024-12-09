import pytest

from classes.many_to_many import Article
from classes.many_to_many import Magazine
from classes.many_to_many import Author

class TestAuthor:
    """Author in many_to_many.py"""

    def test_has_name(self):
        """Author is initialized with a name"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_2, magazine, "Dating life in NYC")

        assert author_1.name == "Carry Bradshaw"
        assert author_2.name == "Nathaniel Hawthorne"

    def test_name_is_immutable_string(self):
        """author name is of type str and cannot change"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert isinstance(author_1.name, str)
        assert isinstance(author_2.name, str)

        # Ensure name can't be changed to non-string
        with pytest.raises(Exception):
            author_1.name = 2

        assert author_1.name == "Carry Bradshaw"
        assert author_2.name == "Nathaniel Hawthorne"

    def test_name_len(self):
        """author name is longer than 0 characters"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert len(author_1.name) > 0
        assert len(author_2.name) > 0

        # Invalid empty name test
        with pytest.raises(Exception):
            Author("")

    def test_has_many_articles(self):
        """author has many articles"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine, "How to wear a tutu with style")
        article_2 = Article(author_1, magazine, "Dating life in NYC")
        article_3 = Article(author_2, magazine, "How to be single and happy")

        assert len(author_1.articles()) == 2
        assert len(author_2.articles()) == 1
        assert article_1 in author_1.articles()
        assert article_2 in author_1.articles()
        assert article_3 not in author_1.articles()
        assert article_3 in author_2.articles()

    def test_articles_of_type_articles(self):
        """author articles are of type Article"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_2, magazine, "Dating life in NYC")

        assert isinstance(author_1.articles()[0], Article)
        assert isinstance(author_2.articles()[0], Article)

    def test_has_many_magazines(self):
        """author has many magazines"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        magazine_3 = Magazine("GQ", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_2, "2023 Eccentric Design Trends")

        assert magazine_1 in author_1.magazines()
        assert magazine_2 in author_1.magazines()
        assert magazine_3 not in author_1.magazines()

    def test_magazines_of_type_magazine(self):
        """author magazines are of type Magazine"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        magazine_3 = Magazine("GQ", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_2, magazine_2, "2023 Eccentric Design Trends")

        assert isinstance(author_1.magazines()[0], Magazine)
        assert isinstance(author_2.magazines()[0], Magazine)

    def test_topic_areas_are_unique(self):
        """author's topic areas are unique"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        magazine_3 = Magazine("GQ", "Fashion")
        article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author_1, magazine_2, "2023 Eccentric Design Trends")
        article_3 = Article(author_1, magazine_3, "Carrara Marble is so 2020")

        topic_areas = author_1.topic_areas()
        assert len(topic_areas) == len(set(topic_areas))

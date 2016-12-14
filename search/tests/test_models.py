from django.test import TestCase
from search.models import BookCategory, Book


class ModelsTestCase(TestCase):
    """Test suite for the models."""

    def setUp(self):
        self.title = "Harry Porter and the Goblet of Fire"
        self.category_name = "Adventure"
        self.category = BookCategory(name=self.category_name)
        self.category.save()
        self.book = Book(title=self.title, category=self.category)

    def test_category_creation(self):
        """Test whether a book category can be created."""
        self.assertIsInstance(self.category, BookCategory)

    def test_book_creation(self):
        """Test that a book can be created."""
        old_count = Book.objects.count()
        self.book.save()
        new_count = Book.objects.count()
        self.assertNotEquals(old_count, new_count)
        self.assertIsInstance(self.book, Book)


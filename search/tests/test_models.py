from django.test import TestCase
from search.models import BookCategory, Book, DatesMixin


class ModelsTestCase(TestCase):
    """Test suite for the models."""

    def setUp(self):
        """Setup variables."""
        self.title = "Harry Porter and the Goblet of Fire"
        self.category_name = "Adventure"
        self.category = BookCategory(name=self.category_name)
        self.category.save()
        self.book = Book(title=self.title, category=self.category)
        self.dates = DatesMixin()

    def test_category_creation(self):
        """Test whether a book category can be created."""
        self.old_count = BookCategory.objects.count()
        self.new_cat = BookCategory(name="non-fiction")
        self.new_cat.save()
        self.new_count = BookCategory.objects.count()
        self.assertIsInstance(self.category, BookCategory)
        self.assertNotEquals(self.old_count, self.new_count)

    def test_book_creation(self):
        """Test whether a book can be created."""
        self.old_count = Book.objects.count()
        self.book.save()
        self.new_count = Book.objects.count()
        self.assertNotEquals(self.old_count, self.new_count)
        self.assertIsInstance(self.book, Book)
        self.assertEquals(self.book.title, self.title)

    def test_date_mixin(self):
        """Test the date mixin works."""
        self.assertIsInstance(self.dates, DatesMixin)

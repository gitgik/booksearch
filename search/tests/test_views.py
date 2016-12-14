from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from search.models import Book, BookCategory


class SetupMixin(TestCase):
    """A set up mixin for the testing client."""

    def setUp(self):
        """Setup."""
        self.client = Client()
        self.category = BookCategory(name="fiction")
        self.category.save()
        self.book = Book(title="Harry porter", category=self.category)
        self.book.save()


class HomeViewTestCase(SetupMixin):
    """Test case for the home view."""

    def test_user_can_access_homepage(self):
        """Test a user can access the homepage."""
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)


class SearchViewTestCase(SetupMixin):
    """Test case for the search view."""

    def test_user_can_access_searchpage(self):
        """Test a user can access the search page."""
        response = self.client.get(reverse('search'))
        self.assertEquals(response.status_code, 200)

    def test_user_can_search_by_title_and_category(self):
        """Test user can search by title."""
        data = {'title': 'harry porter', 'category': self.category.pk}
        response = self.client.post(reverse('search'), data)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.book.title, response.content)



from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class SetupMixin(TestCase):
    """A set up mixin for the testing client."""

    def setUp(self):
        """Setup."""
        self.client = Client()


class HomeViewTestCase(TestCase):
    """Test case for the home view."""

    def test_user_can_access_homepage(self):
        """Test a user can access the homepage."""
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)


class SearchViewTestCase(TestCase):
    """Test case for the search view."""

    def test_user_can_access_searchpage(self):
        """Test a user can access the search page."""
        response = self.client.get(reverse('search'))
        self.assertEquals(response.status_code, 200)

    def test_user_can_search_by_title(self):
        """Test user can search by title."""
        data = {'title': 'harry porter and', 'choice': 'title'}
        response = self.client.get(reverse('search'), data)
        self.assertEquals(response.status_code, 200)

    def test_user_can_search_by_category(self):
        """Test user can search by category."""
        data = {'title': 'adventure', 'choice': 'category'}
        response = self.client.get(reverse('search'), data)
        self.assertEquals(response.status_code, 200)




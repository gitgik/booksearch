from django.db import models


class DatesMixin(models.Model):
    """A model mixin for date creation and modified."""

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)


class BookCategory(DatesMixin):
    """Model to define the category table."""

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """Return a string representation of the model instance."""
        return "{}".format(self.name)


class Book(DatesMixin):
    """Book model with its fields definitions."""

    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model instance."""
        return "{}".format(self.title)


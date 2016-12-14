from django.forms import ModelForm, ChoiceField, CharField
from .models import Book, BookCategory


class SearchForm(ModelForm):
    """This class defines a form."""

    CHOICES = [('title', 'Title'), ('category', 'Category')]

    class Meta:
        """Meta class to define model and associated field for the form."""

        model = Book
        fields = ['title', 'category']


class CategoryForm(ModelForm):
    """This class defines a categroy form."""
    class Meta:
        """Meta class to define model and associated field for the form."""

        model = BookCategory
        fields = ['name', ]

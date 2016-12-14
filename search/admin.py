from django.contrib import admin
from .models import BookCategory, Book

# Register the models
admin.site.register(Book)
admin.site.register(BookCategory)

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .forms import SearchForm
from .models import Book
from django.core.urlresolvers import reverse


class SearchViewMixin(object):
    """A mixin for the home view."""

    def get_context_data(self, **kwargs):
        """Return the context data for the template."""
        context = super(SearchViewMixin, self).get_context_data(**kwargs)
        context['search_form'] = SearchForm()
        # context['category_form'] = CategoryForm()
        context['results'] = Book.objects.all()[:5]
        return context


class HomeView(SearchViewMixin, ListView):
    """This view handles the home page."""

    template_name = "index.html"

    def get_queryset(self):
        """Get query set."""
        pass

    def post(self, request, *args, **kwargs):
        """Handle the post request from the form."""
        choice = request.POST.get('category')
        search_query = request.POST.get('title')

        if not search_query:
            return redirect(reverse('index'))
        # Check first whether the book belongs to that category
        results = Book.objects.filter(category=choice).filter(title__icontains=search_query)
        return render(request, "results.html", {'results': results})


class SearchView(SearchViewMixin, TemplateView):
    """This view handles the search results."""

    template_name = "results.html"

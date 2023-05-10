from django.urls import path
from .views import SearchResult
app_name='searchapp'
urlpatterns = [
    # Other URL patterns...
    path('search/', SearchResult, name='search'),
]


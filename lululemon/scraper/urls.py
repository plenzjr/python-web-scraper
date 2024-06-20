from django.urls import path
from .views import ProductScraperView


urlpatterns = [
    path('scrape/', ProductScraperView.as_view(), name='scrape'),
]

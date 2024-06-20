
import requests

from django.http import HttpResponse
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from cachetools import cached, TTLCache
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import ProductSerializer


cache = TTLCache(maxsize=100, ttl=600)


@cached(cache)
def fetch_product_data(url):
    """
    Fetch product data from Lululemon API
    """

    # all the fields return a list, but to make it simple,
    # we only need the first element
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        products = data['contents'][0]['mainContent'][0]['contents'][0]['records']
        return [
            {
                'product_name': product['attributes']['product.displayName'][0],
                'category': product['attributes']['product.parentCategory.displayName'][0],
                'image': product['attributes']['product.sku.skuImages'][0],
                'price': product['attributes']['product.price'][0],
                'currency': product['attributes']['currencyCode'][0],
                'url': f"https://shop.lululemon.com{product['attributes']['product.pdpURL'][0]}",
            } for product in products
        ]
    return []


class ProductScraperView(APIView):
    """
    Scrape product data from Lululemon URLs
    """

    @swagger_auto_schema(
        operation_description="Scrape product data from Lululemon URLs",
        responses={
            200: ProductSerializer(many=True),
            500: openapi.Response("Error message", schema=openapi.Schema(type=openapi.TYPE_STRING))
        }
    )
    def get(self, request):
        urls = [
            "https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json",
            "https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json"
        ]
        results = []
        try:
            for url in urls:
                results.extend(fetch_product_data(url))

            serializer = ProductSerializer(results, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def home(request):
    urls = [
        {'name': 'Admin', 'url': reverse('admin:index')},
        {'name': 'API Scrape', 'url': reverse('scrape')},
        {'name': 'Swagger', 'url': reverse('schema-swagger-ui')},
        {'name': 'ReDoc', 'url': reverse('schema-redoc')}
    ]
    html = "<h1>Welcome to the Lululemon Product Scraper API</h1><ul>"
    for url in urls:
        html += f"<li><a href='{url['url']}'>{url['name']}</a></li>"
    html += "</ul>"
    return HttpResponse(html)

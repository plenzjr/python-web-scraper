from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class ProductScraperTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_scrape_products(self):
        response = self.client.get('/api/scrape/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), list)
        self.assertTrue(len(response.json()) > 0)
        for product in response.json():
            self.assertIn('product_name', product)
            self.assertIn('category', product)
            self.assertIn('image', product)
            self.assertIn('price', product)
            self.assertIn('currency', product)
            self.assertIn('url', product)

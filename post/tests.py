from django.test import TestCase
from rest_framework import test

# Create your tests here.


class TestPostViewSet(test.APITestCase):
    def setup(self):
        print("hello world")

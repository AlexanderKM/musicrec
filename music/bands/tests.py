"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *
from views import *


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        
    def testSortSearches(self):
        
        Genre.objects.create(name="Rock")
        genresList = Genre.objects.filter(name="Rock")
        genre1 = genresList[0]
        Band.objects.create(name="Band1", genre=genre1)
        Band.objects.create(name="Band2", genre=genre1)
        band1list = Band.objects.filter(name="Band1")
        band1 = band1list[0]
        band2list = Band.objects.filter(name="Band2")
        band2 = band2list[0]
        Search.objects.create(band=band1)
        Search.objects.create(band=band2)
        Search.objects.create(band=band1)
        
        sortedSearches = getTopSearches()
        
        self.assertGreater(sortedSearches[0][1], sortedSearches[1][1], "The first item in the" +
                           "list has a greater count than the second")
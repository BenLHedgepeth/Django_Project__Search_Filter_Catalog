from django.test import TestCase
from minerals import forms
from django.conf import settings


class TestSearchFormPrompt(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.form = forms.SearchForm()

    def test_search_field_placeholder(self):
        search_placeholder = (self.form.fields
                                ['query'].widget.attrs['placeholder'])
        self.assertEqual(
            "Search mineral info here...", 
            search_placeholder
        )
from random import choice
from django.test import TestCase
from django.http import Http404
from django.urls import reverse
from ..models import Mineral

class MineralListingPage(TestCase):
    '''Verify that filtering minerals by first letter defaults
    to the letter "A" upon requesting the listing page'''

    def test_get_listing_page_default_filter(self):
        response = self.client.get(reverse("minerals:letter_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('minerals/list.html')
        self.assertContains(
            response, 
            '<a href="/minerals/letter/A/" id="active_link">A</a>', html=True
        )

    def test_get_listing_by_letter_b(self):
        response = self.client.get(reverse("minerals:letter_list", kwargs={'query': 'B'}))
        self.assertContains(response, "Brushite")


class MineralDetailView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.mineral_name_200="Armalcolite"
        cls.mineral_name_404="Kryptonite"

    def test_mineral_exists_detail_page(self):
        response = self.client.get(
            reverse("minerals:detail", kwargs={'name': self.mineral_name_200})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("minerals/detail.html")
        self.assertContains(
            response,
            '<h1 class="mineral__name">Armalcolite</h1>', html=True
        )

    def test_invalid_mineral_raises_404(self):
        response = self.client.get(
            reverse("minerals:detail", kwargs={'name': self.mineral_name_404})
        )
        self.assertEqual(response.status_code, 404)

class SearchFormResults(TestCase):

    def test_user_search_query_fail(self):
        response = self.client.get(
            reverse("minerals:search_list"), data={'query': 'Kryptonite'},
            HTTP_REFERER=reverse(
                "minerals:letter_list", kwargs={'query': 'N'}
            ), follow=True
        )
        self.assertRedirects(response, reverse(
                "minerals:letter_list", kwargs={'query': 'N'}
            )
        )
        self.assertTemplateUsed("minerals/list.html")
        self.assertContains(response, "No minerals exist with the provided search.")
          

    def test_user_search_query_results_found(self):
        response = self.client.get(
            reverse("minerals:search_list"), data={'query': 'White'},
            HTTP_REFERER=reverse(
                "minerals:detail", kwargs={'name': 'Sapphirine'}
            ), follow=True
        )
        self.assertTemplateUsed("minerals/search.html")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Afwillite")

    def test_user_search_query_results_found(self):
        response = self.client.get(
            reverse("minerals:search_list"), data={'query': 'Tacos'},
            HTTP_REFERER=reverse(
                "minerals:detail", kwargs={'name': 'Sapphirine'}
            ), follow=True
        )
        self.assertTemplateUsed("minerals/detail.html")
        self.assertContains(response, 'Sapphirine')


class CategoryFilterLinks(TestCase):

    def test_mineral_category_link(self):
        response = self.client.get('minerals:category', kwargs={'category': "Native metal"})
        self.assertTemplateUsed("minerals/list.html")

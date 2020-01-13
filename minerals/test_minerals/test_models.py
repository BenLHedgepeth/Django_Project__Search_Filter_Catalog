
from django.test import TestCase
from minerals.models import Mineral
from django.conf import settings


class MineralInstanceMethods(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.mineral = Mineral.objects.create(
        name="Kryptonite",
    )

    def test_mineral_model_str_method(self):
        self.assertEqual(str(self.mineral), "Kryptonite")

    def test_mineral_url(self):
        self.assertEqual(
            self.mineral.get_absolute_url(), "/minerals/mineral/Kryptonite/"
        )

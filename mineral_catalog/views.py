from django.http import HttpResponseRedirect
from django.urls import reverse


def show_minerals(request):
    return HttpResponseRedirect(reverse("minerals:letter_list"))

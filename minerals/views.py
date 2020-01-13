from random import choice
from string import ascii_uppercase

from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Mineral
from .forms import SearchForm

from .link_names import categories

# Create your views here.
def mineral_list(request, query="A"):
    minerals = get_list_or_404(Mineral, Q(name__startswith=query)|Q(group=query))
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        return HttpResponse(reverse("minerals:search_list"))
    search_form = SearchForm()
    random_mineral = choice(Mineral.objects.all())
    return render(
        request, 
        "minerals/list.html", 
        context={
            'minerals': minerals,
            'random_mineral': random_mineral,
            'query': query,
            'categories': categories,
            'letters': ascii_uppercase,
            'form': search_form,
        }
    )


def mineral_detail_page(request, name):

    mineral = Mineral.objects.filter(name=name).values()
    if not mineral:
        raise Http404("Mineral nowhere to be found")
    else:
        mineral[0].pop('id')
        mineral = {key: value for key, value in mineral[0].items() if value != ""}
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        return HttpResponse(reverse("minerals:search_list"))
    search_form = SearchForm()
    return render(
        request, 'minerals/detail.html', 
        {'mineral': mineral, 'form': search_form, 'letters': ascii_uppercase, 'categories': categories}
    )


def search_list(request):
    search_query = request.GET.get('query')
    matched_minerals = Mineral.objects.filter(
        Q(name__icontains=search_query)|
        Q(image_caption__icontains=search_query)|
        Q(category__icontains=search_query)|
        Q(formula__icontains=search_query)|
        Q(strunz_classification__icontains=search_query)|
        Q(crystal_system__icontains=search_query)|
        Q(unit_cell__icontains=search_query)|
        Q(color__icontains=search_query)|
        Q(crystal_symmetry__icontains=search_query)|
        Q(cleavage__icontains=search_query)|
        Q(mohs_scale_hardness__icontains=search_query)|
        Q(luster__icontains=search_query)|
        Q(streak__icontains=search_query)|
        Q(diaphaneity__icontains=search_query)|
        Q(optical_properties__icontains=search_query)|
        Q(group__icontains=search_query)
    )

    if not matched_minerals:
        messages.info(request, "No minerals exist with the provided search.")
        previous_page = request.META['HTTP_REFERER']
        return HttpResponseRedirect(previous_page)
    else:
        search_form = SearchForm()
        return render(
            request, 'minerals/list.html', 
            {'minerals': matched_minerals, 'form': search_form, 
            'letters': ascii_uppercase, 'categories': categories}
        )

def show_mineral(request):
    mineral = choice(Mineral.objects.all())
    return HttpResponseRedirect(reverse("minerals:detail", kwargs={'name': mineral}))
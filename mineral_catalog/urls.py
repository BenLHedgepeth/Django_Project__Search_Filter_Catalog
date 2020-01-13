"""mineral_catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, re_path, include
from mineral_catalog.views import show_minerals
from minerals import views


mineral_patterns = ([
    path('letter/A/', views.mineral_list, name="letter_list"),
    re_path(r'letter/(?P<query>([A-Z]))/', views.mineral_list, name="letter_list"),
    path('category/<query>/', views.mineral_list, name="category_list"),
    path('search/', views.search_list, name="search_list"),
    path("mineral/<name>/", views.mineral_detail_page, name="detail"),
    path("mineral/random", views.show_mineral, name="random")
], "minerals")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", show_minerals, name="show_minerals"),
    path('minerals/', include(mineral_patterns)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

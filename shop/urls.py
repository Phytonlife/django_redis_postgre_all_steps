
from django.urls import path
from shop import views

urlpatterns = [
    path("",views.index),
    path("category/<slug:cat_slug>",views.categories_by_slug)
]

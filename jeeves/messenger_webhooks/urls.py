from django.conf.urls import url

from . import views

urlpatterns = [
    url("/messages$", views.register_view),
]

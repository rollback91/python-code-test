from django.conf.urls import url
from .views import show_reactions

urlpatterns = [
    url(r'^(?P<id>[0-9]+)', show_reactions, name='episode-reactions'),
]
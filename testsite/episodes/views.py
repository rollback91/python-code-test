from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Episode
from itertools import chain
from operator import attrgetter
# Create your views here.


def show_reactions(request, id):
    episode = get_object_or_404(Episode, pk=id)
    img_reactions = episode.imagereaction_set.all().filter(deleted=False)
    tweet_reactions = episode.tweetreaction_set.all().filter(deleted=False)

    reactions = sorted(chain(img_reactions, tweet_reactions), key=attrgetter('created_at'))

    context = dict(reactions=reactions)

    return render(request, 'episode.html', context=context)

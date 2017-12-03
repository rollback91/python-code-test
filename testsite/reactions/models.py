from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


reaction_fk = getattr(settings, 'REACTIONS_FK', None)


class AbstractReaction(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField()
    deleted = models.BooleanField(default=False)

    if reaction_fk:
        reacted_to = models.ForeignKey(reaction_fk, null=True, blank=True)

    class Meta:
        abstract = True


class ImageReaction(AbstractReaction):
    image = models.ImageField()


class TweetReaction(AbstractReaction):
    text = models.CharField(max_length=150)

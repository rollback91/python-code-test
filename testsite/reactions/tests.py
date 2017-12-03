from django.test import TestCase
from .models import TweetReaction, ImageReaction
from django.test import Client
from django.core.urlresolvers import reverse


def logged_client():
    client = Client()
    client.login(username='admin', password='admin')
    return client


class ReactionTests(TestCase):
    fixtures = ['test_data.json']

    def test_admin_delete_action(self):
        client = logged_client()
        reaction = TweetReaction.objects.get(pk=1)
        self.assertFalse(reaction.deleted)

        url = reverse('admin:reactions_tweetreaction_changelist')
        data = {'action': 'delete_selected', '_selected_action': '1'}
        response = client.post(url, data, follow=True)

        reaction = TweetReaction.objects.get(pk=1)
        self.assertTrue(reaction.deleted)

    def test_admin_udelete_action(self):
        client = logged_client()
        reaction = TweetReaction.objects.get(pk=3)
        self.assertTrue(reaction.deleted)

        url = reverse('admin:reactions_tweetreaction_changelist')
        data = {'action': 'undelete_selected', '_selected_action': '1'}
        response = client.post(url, data, follow=True)

        reaction = TweetReaction.objects.get(pk=1)
        self.assertFalse(reaction.deleted)

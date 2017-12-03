from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse


def get_episode_rections_response(id):
    client = Client()
    url = reverse('episode-reactions', kwargs={'id':id})
    return client.get(url)


class EpisodeTests(TestCase):
    fixtures = ['test_data.json']

    def test_unexistend_episode_will_return_404(self):
        response = get_episode_rections_response(999)
        self.assertEqual(404, response.status_code)

    def test_episode_will_return_200(self):
        response = get_episode_rections_response(2)
        self.assertEqual(200, response.status_code)

    def test_episode_with_no_reactions_will_display_somenthing(self):
        response = get_episode_rections_response(3)
        self.assertContains(response, 'Nothing ')

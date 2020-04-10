from django.test import SimpleTestCase
from django.urls import reverse, resolve
from . views import HomePageView

class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        # Checks template name
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        # Checks template contents
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        # response = self.client.get('/')
        self.assertNotContains(self.response, 'I should not be there')

    def test_homepage_url_resolves_homepageview(self):
        # ResolverMatch(func=pages.views.HomePageView, args=(), kwargs={},
        #               url_name=home, app_names=[], namespaces=[], route=)
        view = resolve('/')
        self.assertEqual(view.func.__name__,HomePageView.as_view().__name__)


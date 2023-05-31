from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.


class HomePageTests(SimpleTestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get('/pages/home/')
        self.assertEqual(response.status_code, 200)

    def test_url_exists_by_name(self):
        response = self.client.get(reverse("home-page"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("home-page"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):  # new
        response = self.client.get(reverse("home-page"))
        self.assertContains(response, "<h1>Home Page</h1>")


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/pages/about/")
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_url_exists_by_name(self):
        response = self.client.get(reverse("about-page"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("about-page"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):  # new
        response = self.client.get(reverse("about-page"))
        self.assertContains(response, "<h1>About Page</h1>")
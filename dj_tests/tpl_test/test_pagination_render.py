from django.contrib.auth.models import User
from django.http import HttpResponse
from django.test import Client
from django.test import TestCase


class AppPaginationRender(TestCase):
    def setUp(self) -> None:
        self._http = Client()

    def test_pagination_render(self):
        User.objects.create_user("hello")
        User.objects.create_user("world")

        resp = self._http.get("/pagination")
        assert isinstance(resp, HttpResponse)
        assert resp.status_code == 200
        content = resp.content.decode()
        print(content)

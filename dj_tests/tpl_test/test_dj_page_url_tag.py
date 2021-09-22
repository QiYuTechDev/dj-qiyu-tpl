from django.http import HttpResponse
from django.test import Client
from django.test import TestCase


class DjPageUrlTagTestCase(TestCase):
    def setUp(self) -> None:
        self._http = Client()

    def test_dj_page_url(self):
        resp = self._http.get("/dj_page_url?hello=world&page=1")
        assert isinstance(resp, HttpResponse)
        assert resp.status_code == 200
        content = resp.content.decode()
        assert "hello=world" in content
        assert "page=2" in content

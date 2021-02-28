from django.http import HttpResponse
from django.test import Client
from django.test import TestCase


class RstDocTagTestCase(TestCase):
    def setUp(self) -> None:
        self._http = Client()

    def test_app_doc_tag(self):
        resp = self._http.get("/rst_doc")
        assert isinstance(resp, HttpResponse)
        assert resp.status_code == 200
        content = resp.content.decode()
        assert "app_doc" in content
        assert "document" in content
        assert "hello world" in content
        assert "this is a demo" in content
        assert content.count("script") == 2

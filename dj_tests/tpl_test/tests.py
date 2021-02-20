import json

from django.http import HttpResponse
from django.test import Client
from django.test import TestCase


class DemoHTTPTestCase(TestCase):
    def setUp(self) -> None:
        self._http = Client()

    def test_demo_view_json_result(self):
        resp = self._http.get("/demo")
        assert isinstance(resp, HttpResponse)
        assert resp.status_code == 200
        content = resp.content.decode()
        d = json.loads(content)
        assert d["hello"] == "world"

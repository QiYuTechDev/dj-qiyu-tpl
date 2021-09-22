from django.http import HttpResponse
from django.test import Client, TestCase


class PcOrMobileTestCase(TestCase):
    def test_pc(self):
        http = Client()
        resp = http.get("/pc_mobile")
        assert isinstance(resp, HttpResponse)
        assert resp.status_code == 200
        content = resp.content.decode()
        assert "pc" in content

    def test_mobile(self):
        http = Client(HTTP_USER_AGENT="Mobile")
        resp = http.get("/pc_mobile")
        assert isinstance(resp, HttpResponse)
        assert resp.status_code == 200
        content = resp.content.decode()
        assert "mobile" in content

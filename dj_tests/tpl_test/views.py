from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

__all__ = ['demo_view', "app_doc_tag_view"]


def demo_view(request: HttpRequest) -> HttpResponse:
    return JsonResponse(data={"hello": "world"})


def app_doc_tag_view(request: HttpRequest) -> HttpResponse:
    return render(request, "app_doc.html", {"code": "hello"})

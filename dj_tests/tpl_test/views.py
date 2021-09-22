from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

__all__ = ['demo_view', "app_doc_tag_view", "rst_doc_tag_view", "PaginationView", "DjPageUrl"]


def demo_view(request: HttpRequest) -> HttpResponse:
    return JsonResponse(data={"hello": "world"})


rst_code = f"""\
hello world
====================

this is a demo

.. code-block:: c

    int main(int argc, char * argv) {{
        return 0;
    }}
"""


def app_doc_tag_view(request: HttpRequest) -> HttpResponse:
    return render(request, "app_doc.html", {"code": rst_code})


def rst_doc_tag_view(request: HttpRequest) -> HttpResponse:
    return render(request, "rst_doc.html", {"code": rst_code})


def pc_mobile_render(request: HttpRequest) -> HttpResponse:
    return render(request, "pc_mobile.html")


class PaginationView(ListView):
    template_name = 'pagination.html'
    paginate_by = 1

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return User.objects.all()


class DjPageUrl(TemplateView):
    template_name = 'dj_page_url.html'

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

__all__ = ['demo_view', "app_doc_tag_view", "rst_doc_tag_view"]


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

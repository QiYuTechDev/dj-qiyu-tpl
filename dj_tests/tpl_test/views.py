from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

__all__ = ['demo_view', "app_doc_tag_view"]


def demo_view(request: HttpRequest) -> HttpResponse:
    return JsonResponse(data={"hello": "world"})


def app_doc_tag_view(request: HttpRequest) -> HttpResponse:
    rst_code = f"""\
hello world
====================

this is a demo

.. code-block:: c

    int main(int argc, char * argv) {{
        return 0;
    }}
"""
    return render(request, "app_doc.html", {"code": rst_code})

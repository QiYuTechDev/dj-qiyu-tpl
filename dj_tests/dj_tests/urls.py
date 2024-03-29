"""dj_tests URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tpl_test import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # demo view
    path("demo", views.demo_view),
    path("app_doc", views.app_doc_tag_view),
    path("rst_doc", views.rst_doc_tag_view),
    path("pc_mobile", views.pc_mobile_render),
    path("pagination", views.PaginationView.as_view()),
    path("dj_page_url", views.DjPageUrl.as_view()),
]

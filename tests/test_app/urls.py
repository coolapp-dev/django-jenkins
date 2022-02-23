# -*- coding: utf-8 -*-
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView

urlpatterns = [
    re_path(r'^test_click/$', TemplateView.as_view(template_name='test_app/wm_test_click.html'),
        name='wm_test_click')
]

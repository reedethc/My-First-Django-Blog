# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:57:57 2017

@author: G84711
"""

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
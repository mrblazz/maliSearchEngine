# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:31:25 2018

@author: Arvinder Shinh
"""

from django.urls import path

from . import views

urlpatterns = [
    path('UrlSearchForm/', views.UrlSearchForm, name='UrlSearchForm'),
    path('UrlSearchResult/', views.UrlSearchResult, name='UrlSearchResult'),
    path('UrlSearchResult/<str:html_file>/', views.UrlContent, name='UrlContent')
]
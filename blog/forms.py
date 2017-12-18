# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:39:12 2017

@author: G84711
"""

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)                                         
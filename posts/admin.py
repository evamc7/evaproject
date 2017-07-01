# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp", "image"]
	list_display_links = ["updated"]
	list_editable = ["title"]  # esto sirve para poder editar los titulos desde la pagina web
	list_filter = ["updated","timestamp"]
	search_fields = ["title", "content"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)
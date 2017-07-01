from urllib import quote_plus
from django import template
from django.conf.urls import url

register = template.Library()

@register.filter 
def urlify(value):
	return quote_plus(value)
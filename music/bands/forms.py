from .models import *
from django import forms
from django.db.models import Q
from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe
from django.utils.timezone import now

class SearchBandForm(forms.Form):
    """
    Form used for sending a new message to a specific user
    """
    bandName = forms.CharField(max_length=50)
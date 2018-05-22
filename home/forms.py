from django import forms
from django.contrib.admin import widgets
import os

COICE = {
    (0,"CG"),
    (1,"イラスト")
    (3,"ウェブアプリ")
}

form SampleForm(forms.Form):
    select = forms.ChoiceField(label='属性', widget=forms.RadioSelect, choices= CHOICE, initial=0)

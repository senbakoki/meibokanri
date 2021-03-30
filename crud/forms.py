from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import AuthenticationForm 
from .models import Message






class MessageForm(forms.Form):
    teacher_name = forms.CharField(
        label='先生の名前',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )
    time13_1 = forms.CharField(
        label='一時コマ(1)',
        max_length=20,
        widget=forms.TextInput(),
        required=False
    )
    time13_2 = forms.CharField(
        label='一時コマ(2)',
        max_length=20,
        widget=forms.TextInput(),
        required=False
    )
    time14_1 = forms.CharField(
        label='二時半コマ(1)',
        max_length=20,
        widget=forms.TextInput(),
        required=False

    )
    time14_2 = forms.CharField(
        label='二時半コマ(2)',
        max_length=20,
        widget=forms.TextInput(),
        required=False
    )
    time17_1 = forms.CharField(
        label='五時コマ(1)',
        max_length=20,
        widget=forms.TextInput(),
        required=False
    )
    time17_2 = forms.CharField(
        label='五時コマ(2)',
        max_length=20,
        widget=forms.TextInput(),
        required=False
    )
    time18_1 = forms.CharField(
        label='六時半コマ(1)',
        max_length=20,
        widget=forms.TextInput(),
        required=False
    )
    time18_2 = forms.CharField(
        label='六時半コマ(2)',
        max_length=20,
        widget=forms.TextInput(),
        required=False
    )
    time20_1 = forms.CharField(
        label='八時コマ(1)',
        max_length=20,
        widget=forms.TextInput(),
        required=False
    )
    time20_2 = forms.CharField(
        label='八時コマ(2)',
        max_length=20,
        widget=forms.TextInput(),
        required=False
    )
#p


class LoginForm(AuthenticationForm):
    """ログオンフォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  
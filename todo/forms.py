from allauth.account.forms import SignupForm
from django import forms
from .models import Todo, UserProfile

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"


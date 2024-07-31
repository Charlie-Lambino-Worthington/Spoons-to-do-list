from allauth.account.forms import SignupForm
from django import forms
from .models import Todo, UserProfile

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

class CustomSignupForm(SignupForm):
    max_spoons = forms.IntegerField(
        label='Maximum Spoons',
        required=True,
        initial=12,
        help_text='Enter the maximum number of spoons you have.'
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        UserProfile.objects.create(
            user_id=user.id,
            username=user.username,
            max_spoons=self.cleaned_data['max_spoons']
        )
        return user

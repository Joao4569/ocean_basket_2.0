"""Import forms needed for creating forms"""
from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    """This will add custom fields to the standard django
    allauth signup form. """
    first_name = forms.CharField(
        max_length=25, label='First Name')
    last_name = forms.CharField(
        max_length=25, label='Last Name')

    def save(self, request):
        """When saving allocate custom fields to model"""
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

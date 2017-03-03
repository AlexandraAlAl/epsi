from django import forms
from extuser.models import ExtUser

class ExtUserForm(forms.ModelForm):

    class Meta:
        model = ExtUser
        fields = ('firstname', 'lastname', 'name_comp', 'phone')

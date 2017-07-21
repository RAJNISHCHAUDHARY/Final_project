from django import forms
from models import UserModel


class SignUpForms(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = {'Email','Username','Name','Password'}

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = {'Username','Password'}
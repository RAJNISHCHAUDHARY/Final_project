from django import forms
from models import UserModel,PostModel,LikeModel, CommentModel


class SignUpForms(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['Email','Username','Name','Password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['Username','Password']

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields=['image', 'caption']


class LikeForm(forms.ModelForm):

    class Meta:
        model = LikeModel
        fields=['post']


class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ['comment_text', 'post']
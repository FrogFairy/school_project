from django import forms
from django.contrib.auth.models import User
from .models import Reviews, Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ReviewForm(forms.ModelForm):
    text = forms.Textarea()
    rating = forms.IntegerField()

    class Meta:
        model = Reviews
        fields = ['text', 'rating']


class ProfileForm(forms.ModelForm):
    role = forms.Textarea()
    school_id = forms.IntegerField()

    class Meta:
        model = Profile
        fields = ['role', 'school_id']
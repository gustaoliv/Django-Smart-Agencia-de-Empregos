from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Candidate
from django import forms


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser 
        fields = ('first_name', 'last_name', 'username',)
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        user.email = self.cleaned_data.get('username')
        if commit:
            user.save()
        return user

        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')



class CandidateCreateForm(UserCreationForm):
    class Meta:
        model = Candidate;
        fields = ('first_name', 'last_name', 'username',)
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        user.email = self.cleaned_data.get('username')
        if commit:
            user.save()
        return user


class CandidateChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')


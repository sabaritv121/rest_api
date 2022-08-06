from django.contrib.auth.forms import UserCreationForm
from django import forms
from studentapp.models import Login, Student


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2',)


class StudentRegister(forms.ModelForm):

    # department = forms.ModelChoiceField(queryset=Department.objects.all())

    class Meta:
        model = Student
        fields = ('name', 'address', 'school', 'course')

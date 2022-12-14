from django import forms
from django.core import validators
from .models import User, Course


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
        'name' : forms.TextInput(attrs = {'class': 'form-control'}),
        'email': forms.EmailInput(attrs = {'class': 'form-control'}),
        'password': forms.PasswordInput(render_value=True, attrs = {'class': 'form-control'})
        }
#second form

class StudentCourseRegistration(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name_course', 'email_course', 'password_course']
        widgets = {
        'name_course' : forms.TextInput(attrs = {'class': 'form-control'}),
        'email_course': forms.EmailInput(attrs = {'class': 'form-control'}),
        'password_course': forms.PasswordInput(render_value=True, attrs = {'class': 'form-control'})
        }





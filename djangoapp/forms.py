from django import forms
from django.contrib.auth.models import User

class  userreg(forms.Form):
    class Meta:
        model=User#model used to crate form
        fields=['username','first_name','last_name','email','password']

class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=20,widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','confirm']


class userlogin(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=15)





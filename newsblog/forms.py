from django import forms
from .models import userinfo
from crispy_forms.helper import FormHelper


class userForm(forms.ModelForm):
    class Meta:
        model = userinfo
        fields = ( 'title'  , 'name'  , 'mobile', 'message', 'date_birth','gender','marital_status','addressLine1','addressLine2','state','city')
        


  

        

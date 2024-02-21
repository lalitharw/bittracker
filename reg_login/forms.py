from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required = True)

    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)

    #     self.fields["email"].disabled = True
    #     # self.fields["email"].widget = forms.HiddenInput()
    
    class Meta:
        model = User
        fields = ['username','email']
        labels ={
            'username':'Name',
        }

    def clean_username(self):
        valname = self.cleaned_data['username']
        if ' ' in valname:
            raise forms.ValidationError('Space is not allowed in username')
        
      

        elif len(valname) <= 4:
            raise forms.ValidationError("Username should be more than 4 characters")
        return valname
    

    


class LoginForm(AuthenticationForm):
   
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username':forms.TextInput(attrs={'placeholder':"Enter username",'class':'input'})
        }

from django import forms
from .models import *
from datetime import date



class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'required':'True'}))
    last_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'required':'True'}))
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields["user"].disabled = True
        self.fields["user"].widget = forms.HiddenInput()
        self.fields["user"].label = ''
    class Meta:
        model = Profile
        fields = ["user", "first_name", "last_name",'Confirm_email']
        





class HabitForm(forms.ModelForm):
    title = forms.CharField(required=True)
    goal = forms.IntegerField(required=True)
    goal_unit = forms.CharField(required=True)
 
    class Meta:
        model = Habit
        fields = ["title","goal","goal_unit"]

    def clean_title(self):
        valname = self.cleaned_data['title']
        block = ['#','&','@','_','+']
        for b in block:
            if b in valname:
                raise forms.ValidationError('Invalid use of character')
        return valname

   
        
      
            
    
class DateInput(forms.DateInput):
    input_type = 'date'

class HabitLogForm(forms.ModelForm):
  
    date = forms.DateField(label='',disabled=True)
    track_unit = forms.IntegerField(required=True)
    def __init__(self, *args, **kwargs):
        super(HabitLogForm, self).__init__(*args, **kwargs)
        self.fields["habit"].disabled = False
        self.fields["habit"].widget = forms.HiddenInput()
        self.fields["habit"].label = ''


    class Meta:
        model = HabitLog
        fields = ['habit',"date", "track_unit"]




    

     

    



    


   
from django import forms
# from django.forms.forms import Form

# Here we will create the validations
def nameVal(value):
    if len(value) <5 :
        raise forms.ValidationError('The name must contain atleast 5 letters')


def emailVal(value):
    if len(value) <5 :
        raise forms.ValidationError('Email must contain atleast 5 letters')

def passVal(value):
    if len(value) < 5 :
        raise forms.ValidationError('Password must contain atleast 5 letters')

# Create the forms here
class mainForm(forms.Form):
    name = forms.CharField(validators=[nameVal] ,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(validators= [emailVal],widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(validators= [passVal] ,widget=forms.PasswordInput(render_value=True ,attrs={'class' : 'form-control'}))
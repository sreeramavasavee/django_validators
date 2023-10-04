from django import forms

def check_for_a(value):
    if value[0].lower() in 'a':
        raise forms.ValidationError('name starts with a')
    
def check_for_len(value):
    if len(value)<5:
       raise forms.ValidationError('length is less than')
    
class studentform(forms.Form):
    sname=forms.CharField(max_length=50,validators=[check_for_a,check_for_len])
    sid=forms.IntegerField()
    sage=forms.IntegerField()
    semail=forms.EmailField(validators=[check_for_a,check_for_len])
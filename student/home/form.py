from django import forms
from .models import Student
    
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {

        'name':'Student Name', 
        'dob' :'Date Of Birth',
        'physics_marks' :'Physics marks',
        'chemistry_marks' :'Chemistry marks', 
        'maths_marks' : 'Maths marks', 
        'cs_marks' : 'Cs marks'
        }
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'})
        }
from django import forms

REASONS = (
    ("question", "Question"),
    ("comment", "Comment"),
    ("suggestion", "Suggestion"),
    ("employment", "Employment"),
    ("other", "Other"),
)

class ReservationForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget)
    time = forms.TimeField(label='Time Field', label_suffix=" : ",
                             required=True, disabled=False, input_formats=["%H:%M:%S"],
                             widget=forms.TimeInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    reason = forms.ChoiceField(choices=REASONS, required=True)
    details = forms.CharField(widget=forms.Textarea, required=True)

class DateForm(forms.Form):
    date=forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

class SurveyForm(forms.Form):
    pass

    
    
        

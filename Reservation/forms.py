from django import forms
from .models import MeetingRoom

"""
class MeetingRoomForm(forms.ModelForm):
    class Meta:
        model = MeetingRoom
        fields = ['mrName', 'avail', 'timeCharge', 'halfCharge', 'dayCharge']

class MRChargeForm(forms.Form):
    timeCharge = forms.BooleanField
    halfCharge = forms.BooleanField
    dayCharge = forms.BooleanField
    """
from django import forms
from .models import hospital

class hospitalform(forms.ModelForm):
	class Meta:
		model = hospital
		fields = '__all__'
		
# from django import forms
# from .models import Workshop
# from django.forms.widgets import SelectDateWidget
# from django.utils import timezone
# import datetime


# class workshopform(forms.ModelForm):

# 	start_date = forms.DateField(widget=SelectDateWidget(),initial=timezone.now())
# 	start_time = forms.TimeField(widget=forms.TimeInput(format='%I:%M %p'))
# 	end_date = forms.DateField(widget=SelectDateWidget(), initial=timezone.now())
# 	end_time = forms.TimeField(widget=forms.TimeInput(format='%I:%M %p'))

# 	def clean_start_date(self):
# 		start_date = self.cleaned_data['start_date']
# 		if start_date < datetime.date.today():
# 			raise forms.ValidationError("The date cannot be in the past!")
# 		return start_date

# 	def clean_end_date(self):
# 		end_date = self.cleaned_data['end_date']
# 		if end_date < datetime.date.today():
# 			raise forms.ValidationError("The date cannot be in the past!")
# 		return end_date


# 	class Meta:
# 		model = workshop
		
# 		exclude = ['']



from django import forms
from .models import ArtistProfile
from django.forms.widgets import SelectDateWidget

class ArtistForm(forms.ModelForm):

	dob = forms.DateField(widget=SelectDateWidget(years=range(1950,2016)))

	def clean_mobile_no(self):
		mobile_no = self.cleaned_data['mobile_no']
		if (mobile_no.isalpha()):
			raise forms.ValidationError("Please enter a valid mobile number!")
		return mobile_no


	class Meta:
		model = ArtistProfile
		exclude = ['']

	def save(self,commit=False):
		artist = super(ArtistForm,self).save(commit=False)
		artist.dob = self.cleaned_data["dob"]
		return artist
from django import forms

CHOICES=[('single_host','Single host'),
         ('multiple_host ','Multiple hosts')]

class SentimentForm(forms.Form):

	title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Enter Title'}))
	input_sentiment = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'placeholder':'Enter Youtube Video URL'}))
	hosts = forms.ChoiceField(choices = CHOICES)
	#files = forms.FileField(max_length=100)

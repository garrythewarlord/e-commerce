from django import forms



class fulfillForm(forms.Form):
	firstName = forms.CharField(label='First Name')
	secondName = forms.CharField(label='Second Name')
	streethouseNumber = forms.CharField(label='Street, House Nr.')	
	city = forms.CharField(label="City")
	postal = forms.CharField(label='Postal Code')		
	phone = forms.CharField(label='Phone number: ', initial='+370')


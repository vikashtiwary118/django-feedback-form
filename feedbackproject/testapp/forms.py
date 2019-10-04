from django import forms
# class FeedBackForm(forms.Form):
# 	name=forms.CharField()
# 	rollno=forms.IntegerField()
# 	email=forms.EmailField()
# 	feedback=forms.CharField(widget=forms.Textarea)

#now for form validation
# explicit validator
# class FeedBackForm(forms.Form):
# 	name=forms.CharField()
# 	rollno=forms.IntegerField()
# 	email=forms.EmailField()
# 	feedback=forms.CharField(widget=forms.Textarea)

# 	#name validation for greater than 4 length
# 	def clean_name(self):
# 		inputname=self.cleaned_data['name']
# 		if len(inputname)<4:
# 			raise forms.ValidationError('The length of name should be greater than four')
# 		return inputname

# 	def clean_rollno(self):
# 		inputrollno=self.cleaned_data['rollno']
# 		print(inputrollno)
# 		return inputrollno

# 	def clean_email(self):
# 		inputemail=self.cleaned_data['email']
# 		print(inputemail)
# 		return inputemail
# 	def clean_feedback(self):
# 		inputfeedback=self.cleaned_data['feedback']
# 		print(inputfeedback)
# 		return inputfeedback


# now implicit validation
from django.core import validators

# def start_with_d(value):
# 	# if value[0].lower()!='d':
# 	# 	raise forms.ValidationError('names hould be start "d" ')
# 	if value[0].isalpha()!=True:
# 		raise forms.ValidationError('names hould be contains only alpha ')#gmail varification using function

# def gmail_varification(value):
# 	if value[len(value)-9:]!='gmail.com':
# 		raise forms.ValidationError('Must be gmail')

# class FeedBackForm(forms.Form):
# 	name=forms.CharField(validators=[start_with_d])
# 	rollno=forms.IntegerField()
# 	email=forms.EmailField(validators=[gmail_varification])
# 	feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])#Here the maximum allowed charechter is 40



#total form validation
# class FeedBackForm(forms.Form):
# 	name=forms.CharField()
# 	rollno=forms.IntegerField()
# 	email=forms.EmailField()
# 	password=forms.CharField(widget=forms.PasswordInput)
# 	rpassword=forms.CharField(label='Password(Again)',widget=forms.PasswordInput)
# 	feedback=forms.CharField(widget=forms.Textarea)

# 	def clean(self):
# 		print('Total Form Validation')
# 		cleaned_data=super().clean()
# 		inputname=cleaned_data['name']
# 		inputpassword=cleaned_data['password']
# 		inputrpassword=cleaned_data['rpassword']
# 		if inputpassword!=inputrpassword:
# 			raise forms.ValidationError('Password not matched')
# 		if len(inputname)<10:
# 			raise forms.ValidationError('Name should contains compalsary 10 charachter')
# 		inputrollno=cleaned_data['rollno']
# 		if len(str(inputrollno))!=3:
# 			raise forms.ValidationError('rollno shuld contains exactly 3 digits')



###Bot varification
class FeedBackForm(forms.Form):
	name=forms.CharField()
	rollno=forms.IntegerField()
	email=forms.EmailField()
	password=forms.CharField(widget=forms.PasswordInput)
	rpassword=forms.CharField(label='Password(Again)',widget=forms.PasswordInput)
	feedback=forms.CharField(widget=forms.Textarea)
	bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

	def clean(self):
		print('Total Form Validation')
		cleaned_data=super().clean()
		bot_handler_value=cleaned_data['bot_handler']
		if len(bot_handler_value)>0:
			raise forms.ValidationError('Thanks Bot!!!')
		





	
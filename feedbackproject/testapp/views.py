from django.shortcuts import render
from . import forms
# Create your views here.

def thankyou_view(request):
	return render(request,'testapp/thankyou.html',{'name':form.cleaned_data['name']})


# def feedback_view(request):
# 	form=forms.FeedBackForm()
# 	if request.method=='POST':
# 		form=forms.FeedBackForm(request.POST)
# 		if form.is_valid():
# 			print("Form validation succes and print feedback info")
# 			print("student name",form.cleaned_data['name'])
# 			print("student rollno",form.cleaned_data['rollno'])
# 			print("student email",form.cleaned_data['email'])
# 			print("student feedback",form.cleaned_data['feedback'])
# 			return render(request,'testapp/thankyou.html',{'name':form.cleaned_data['name']})
					
# 	return render(request,'testapp/feedback.html',{'form':form})


def feedback_view(request):
	if request.method=='GET':
		form=forms.FeedBackForm()
		
	if request.method=='POST':
		form=forms.FeedBackForm(request.POST)
		if form.is_valid():
			print("Form validation succes and print feedback info")
			print("student name",form.cleaned_data['name'])
			print("student rollno",form.cleaned_data['rollno'])
			print("student email",form.cleaned_data['email'])
			print("student feedback",form.cleaned_data['feedback'])
			return render(request,'testapp/thankyou.html',{'name':form.cleaned_data['name']})
	return render(request,'testapp/feedback.html',{'form':form})


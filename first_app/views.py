from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
# def index(request):
# 	return HttpResponse("Hello World!")

def home(request):
	return render(request, 'first_apps/home.html')          #this is templates code
	# return HttpResponse("<h1>Hello Their Friend</h1>")   this is for url code

def about(request):
	return render(request, 'first_apps/about.html') 


def password(request):

	chracter = list("abcdefghijklmnopqrstuvwxyz")

	if request.GET.get('uppercase'):
		chracter.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

	if request.GET.get('numbers'):
		chracter.extend(list("0123456789"))

	if request.GET.get('special'):
		chracter.extend(list("<?!@#$%^&*"))


	length = int(request.GET.get('length',10))  

	thepassword = ''

	for x in range(length):
		thepassword+=random.choice(chracter)

	return render(request, 'first_apps/password.html',{'password':thepassword})
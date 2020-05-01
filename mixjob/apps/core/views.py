from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'inicio.html')

def control(request):
	return render(request, 'control.html')

def recreacion(request):
	return render(request, 'recreacion.html')
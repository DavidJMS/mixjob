from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.shortcuts import render

# Create your views here.
def login_to_plataform(request):
	if request.method == 'POST':
		print(request.POST)
		username = request.POST['usuario']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			pass
	return render(request, 'user/login.html')
from django.shortcuts import render, redirect
from.forms import Usuarioform

# Create your views here.
def criar_usuario(request):
	form = Usuarioform(request.POST)
	if request.method =="POST":
		form = Usuarioform(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save()
			obj.save()
		return redirect('login')
	return render(request, 'usuarios/form_usuario.html', {'form':form})
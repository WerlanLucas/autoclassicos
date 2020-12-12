from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import hospitalform
from .models import hospital
from django.contrib import messages

# Create your views here.

def index(request):
    #return  HttpResponse("<h1>Aqui é o index<h1>")
    return render(request, 'hospitais/index.html')

def hospitais(request):
    #return HttpResponse("<h1>Aqui é área de hospital<h1>")
    hospitais = hospital.objects.all()
    busca = request.GET.get('search')
    if busca:
    	hospitais = hospital.objects.filter(nome_hospital__icontains = busca)
    return render(request, 'hospitais/hospitais.html', {'hospitais':hospitais})

def editar(request, id):
	hosp = get_object_or_404(hospital, pk=id)
	form = hospitalform(instance=hosp)
	if(request.method=="POST"):
		form=hospitalform(request.POST,request.FILES, instance=hosp)
		
		if form.is_valid():
			form.save()
			return redirect('hospitais')

		else:

			return render(request, "hospitais/editar_hospitais.html", {'form':form, 'hosp':hosp})
	else:
		return render(request, 'hospitais/editar_hospitais.html', {'form':form, 'hosp':hosp})


def deletar(request, id):
		hosp = get_object_or_404(hospital, pk=id)
		if request.method == "POST":
			hosp.delete()
			return redirect('hospitais')
		return render(request, "hospitais/deletar_hospital.html",{'hosp':hosp})


def criar_hospital(request):
	form = hospitalform(request.POST)
	if request.method == "POST":
		form = hospitalform(request.POST, request.FILES)
	if form.is_valid():
		hosp = form.save()
		hosp.save()
		messages.success(request, 'Loja inserida com sucesso!')
		form = hospitalform()
	return render(request, 'hospitais/criar_hospitais.html',{'form':form})






	
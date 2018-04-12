from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Articulo

def like(request,  id, accion):
	#Update
	#1.crear objeto, 2.editar obejeto, 3.guardar objeto.
	#paso 1
	art = Articulo.objects.get(pk=id)
	#paso 2
	if accion == 'like':
		art.likes += 1
	else:
		art.dislike += 1

	#paso 3
	art.save()

	return HttpResponseRedirect(reverse('articulo', args=[art.slug]))

def articulo(request, slug):
	#es un where
	art = Articulo.objects.get(slug=slug)

	return render(request, 'articulo.html', {'articulo':art})

def index(request):
	
	#SELECT * FROM Articulos(es lo q aremos con el siguiente codigo), Order by id Dec
	articulos = Articulo.objects.all().order_by('-id')

	return render(request, 'index.html', {'articulos':articulos})

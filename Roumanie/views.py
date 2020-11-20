from django.shortcuts import render, get_object_or_404
from .models import Roumanie

def all_ro(request):
	blogros = Roumanie.objects.all()
	return render(request, 'all_ro.html', {'blogros':blogros})

def detailro(request, the_slug):
	blog2 = get_object_or_404(Roumanie, slug = the_slug)
	return render(request, 'detailbuster.html', {'blog':blog2})


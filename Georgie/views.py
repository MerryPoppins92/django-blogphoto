from django.shortcuts import render, get_object_or_404
from .models import Georgie

def all_go(request):
	bloggos = Georgie.objects.all()
	return render(request, 'all_go.html', {'bloggos':bloggos})

def detailgo(request, the_slug):
	blog2 = get_object_or_404(Georgie, slug = the_slug)
	return render(request, 'detailbuster.html', {'blog':blog2})
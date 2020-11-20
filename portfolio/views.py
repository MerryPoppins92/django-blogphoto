from django.shortcuts import render
from .models import project

def home(request):
	
	proj1 = project.objects.all()[0]
	proj2 = project.objects.all()[1]
	proj3 = project.objects.all()[2]
	return render(request, 'portfolio/home.html', {'proj3':proj3,'proj1':proj1,'proj2':proj2})

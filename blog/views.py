from django.shortcuts import render, get_object_or_404
from .models import Blog, Blogbuster

def all_blogs(request):
	blogbusters = Blogbuster.objects.all()
	return render(request, 'all_blogs.html', {'blogbusters':blogbusters})

def detailbuster(request, the_slug):
	blog1 = get_object_or_404(Blogbuster, slug = the_slug)
	return render(request, 'detailbuster.html', {'blog':blog1})

# def detail(request, blog_id):
# 	blog = get_object_or_404(Blog, pk = blog_id)
# 	return render(request, 'detail.html', {'blog':blog})
# def detail(request, the_slug):
# 	blog1 = get_object_or_404(Article, slug = the_slug)
# 	return render(request, 'detail.html', {'blog':blog1})

# def all_blogs(request):
# 	blogs = Blog.objects.all()
# 	return render(request, 'all_blogs.html', {'blogs':blogs})

# def all_blogbusters(request):
# 	blogbusters = Blogbuster.objects.all()
# 	return render(request, 'all_blogbusters.html', {'blogbusters':blogbusters})
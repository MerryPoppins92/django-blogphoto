from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'blogbuster'

urlpatterns = [
    path('', views.all_blogs, name="all_blogs"),
    path('<slug:the_slug>/', views.detailbuster, name="detailbuster"),

]
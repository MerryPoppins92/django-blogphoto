from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'bloggo'

urlpatterns = [
    path('', views.all_go, name="all_go"),
    path('<slug:the_slug>/', views.detailgo, name="detailgo"),

]
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'blogro'

urlpatterns = [
    path('', views.all_ro, name="all_ro"),
    path('<slug:the_slug>/', views.detailro, name="detailro"),

]
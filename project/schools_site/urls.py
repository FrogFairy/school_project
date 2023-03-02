from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'schools_site'

urlpatterns = [
	path('', views.home, name='home'),
	path('<slug:url>/', views.school_page, name='school_page')
]

urlpatterns += staticfiles_urlpatterns()
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from project.settings import LOGOUT_REDIRECT_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': LOGOUT_REDIRECT_URL}, name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('<slug:url>/add_review', user_views.add_review, name="add_review"),
    path('', include('schools_site.urls', namespace='schools_site')),
]
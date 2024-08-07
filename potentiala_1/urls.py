from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=''), name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('delete/<int:list_id>/', views.delete, name='delete'),
    path('toggle/<int:list_id>/', views.toggle, name='toggle'),
]

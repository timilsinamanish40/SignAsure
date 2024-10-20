from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Import for login/logout views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('', include('verifier.urls')),  # Include verifier app's URLs
    path('accounts/login/', auth_views.LoginView.as_view(template_name='verifier/login.html'), name='login'),  # Custom login view
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view
]

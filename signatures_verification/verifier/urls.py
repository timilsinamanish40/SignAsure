from django.urls import path
from .views import home, register, upload_signature, success

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('register/', register, name='register'),
    path('upload_signature/', upload_signature, name='upload_signature'),  # Signature upload page
    path('success/', success, name='success'),  # Success page
]

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, SignatureUploadForm

def home(request):
    if request.user.is_authenticated:
        return redirect('upload_signature')  # Redirect to upload page if logged in
    return render(request, 'verifier/home.html')  # Render home page if not logged in

def register(request):
    if request.user.is_authenticated:
        return redirect('upload_signature')  # Redirect to upload page if already logged in

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create user instance
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Save user to the database
            login(request, user)  # Log in the user
            return redirect('upload_signature')  # Redirect to upload page
    else:
        form = UserRegistrationForm()  # Display empty form

    return render(request, 'verifier/register.html', {'form': form})  # Render register page

@login_required
def upload_signature(request):
    if request.method == 'POST':
        form = SignatureUploadForm(request.POST, request.FILES)
        if form.is_valid():
            signature = form.save(commit=False)  # Create signature instance
            signature.user = request.user  # Assign the logged-in user to the signature
            signature.save()  # Save the signature to the database
            return redirect('success')  # Redirect to success page
    else:
        form = SignatureUploadForm()  # Display empty form

    return render(request, 'verifier/upload_signature.html', {'form': form})  # Render upload page

@login_required
def success(request):
    
    return render(request, 'verifier/success.html')  # Render success page

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount

@login_required
def profile_view(request):
    social_accounts = SocialAccount.objects.filter(user=request.user)
    return render(request, 'profile.html', {'social_accounts': social_accounts})

def socialaccount_login(request, provider):
    # Implement your logic to handle social media login here
    # Redirect to the social media login URL for the specified provider
    if provider == 'google':
        # Replace 'google_login_url' with the actual URL pattern or view function for Google login
        return redirect('google_login')  # Replace 'google_login' with the correct name
    elif provider == 'facebook':
        # Replace 'facebook_login_url' with the actual URL pattern or view function for Facebook login
        return redirect('facebook_login')  # Replace 'facebook_login' with the correct name
    # Add other social media login providers as needed
    # If the provider is not recognized, you can redirect to the login page
    return redirect('login')

def logout_view(request):
    return redirect('login')

def login_view(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'home.html')
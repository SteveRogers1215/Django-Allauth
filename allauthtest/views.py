from django.shortcuts import render
from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User  # Import User model

def register(request):
    form = SignupForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    return render(request, 'dashboard.html')

class ChangeUsername(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ['username']
    template_name = 'change_username.html'
    success_message = "Username updated successfully"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('account_login')  # or wherever you want to redirect
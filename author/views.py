from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from car.models import ProfileCar
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from car.models import ProfileCar
from django.contrib.auth.views import LoginView,LogoutView


# Create your views here.



@login_required
def profile(request):
    
    data = ProfileCar.objects.filter(author = request.user)
    
    return render(request, 'profile.html',  { 'data' : data, 'type': 'Profile Page'})




def user_register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            messages.success(request, 'Account created Successfully')
            register_form.save()
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form': register_form, 'type': 'Register'})


class UserLoginView(LoginView):
    template_name = 'register.html'
    
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    




class UserLogoutView(LogoutView):
     def get_success_url(self):
        messages.success(self.request, 'Logged out successfully')
        return reverse_lazy('home')
     





@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            messages.success(request, 'Account Updated Successfully')
            profile_form.save()
            return redirect('edit_profile')
    else:
        profile_form = forms.ChangeUserForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': profile_form, 'type':'Update your Profile'})



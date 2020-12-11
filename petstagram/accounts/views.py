from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import generic as views

from petstagram.accounts.forms import SignUpForm, UserProfileForm
from petstagram.accounts.models import UserProfile


# def page_not_found(request):
#     return render(request, 'not-found.html')


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'profile_user': user,
            'profile': user.userprofile,
            'pets': user.userprofile.pet_set.all(),
            'form': UserProfileForm(),
        }
        return render(request, 'accounts/user_profile.html', context)
    else:
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('current user profile')
        return redirect('current user profile')


# def signup_user(request):
#     if request.method == 'GET':
#         context = {
#             'form': SignUpForm(),
#         }
#         return render(request, 'accounts/signup.html', context)
#     else:
#         # Pesho - 5FYzfbDQNr9GUdV
#         form = SignUpForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             profile = UserProfile(
#                 user=user,
#             )
#             profile.save()
#
#             login(request, user)
#             return redirect('current user profile')
#
#         context = {
#             'form': form,
#         }
#         return render(request, 'accounts/signup.html', context)


class SignUpView(views.CreateView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('current user profile')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return valid


def signout_user(request):
    logout(request)
    return redirect('index')

from django.urls import path, include

from petstagram.accounts.views import user_profile, SignUpView, SignOutView, SignInView  # , signup_user, signout_user

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', user_profile, name='current user profile'),
    path('profile/<int:pk>/', user_profile, name='user profile'),
    path('signin/', SignInView.as_view(), name='signin user'),
    # path('signup/', signup_user, name='signup user'),
    path('signup/', SignUpView.as_view(), name='signup user'),
    # path('signout', signout_user, name='signout user'),
    path('signout', SignOutView.as_view(), name='signout user'),
]

from .receivers import *

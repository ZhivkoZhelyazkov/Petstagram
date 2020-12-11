from django.urls import path

from petstagram.common.views import LandingPage  # landing_page,

urlpatterns = [
    # path('', landing_page, name='index'),
    path('', LandingPage.as_view(), name='index'),
]
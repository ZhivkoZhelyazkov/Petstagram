from django.views import generic as views
from django.shortcuts import render


# def landing_page(request):
#     return render(request, 'landing_page.html')


class LandingPage(views.TemplateView):
    template_name = 'landing_page.html'

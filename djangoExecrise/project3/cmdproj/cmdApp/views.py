from django.views.generic import ListView

from .models import tableone

class HomePageView(ListView):
    model=tableone
    template_name='home.html'

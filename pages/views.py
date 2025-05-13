from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

# Option 1: function based
def home_page_view(request):
    return render(request, "home.html")

# Option 2: class based
class HomePageView(View):
    def get(self, request):
        return render(request, "home.html")

# option 3: generic class based
class HomePageView2(TemplateView):
    template_name = "home.html"

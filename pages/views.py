from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView
from datetime import datetime


# Option 1: function based
# def home_page_view(request):
    # print(request.META['HTTP_USER_AGENT'])
    # print(request.META['REMOTE_ADDR'])
    # html_response = HttpResponse('<h1>hello world</h1>')
    # html_response.write('<div>again</div>')
    # html_response.set_cookie('my_cookie', 'cookie_value')
    # print(request.COOKIES)
    # json_response = JsonResponse({'status': 'success', 'message': 'Hello'})
    # print(json_response)
    # json_response.delete_cookie('my_cookie')

    # return json_response

def home_page_view(request):
    print(request.GET) # http://127.0.0.1:8000/?key=val
    context = {
        'title': 'Welcome',
        'today': datetime.now(),
        'numbers': [1, 2, 3],
        'dic': {"one": 1, "two":2},
    }
    # set_cookie('my_cookie', 'cookie_value')
    res = render(request, 'home.html', context)
    res.set_cookie('my_cookie', 'cookie_value')
    print(res)
    return res

# Option 2: class based
class HomePageView(View):
    def get(self, request):
        return render(request, "home.html")

# option 3: generic class based
class HomePageView2(TemplateView):
    template_name = "home.html"


from django.http import HttpResponseForbidden

class ActiveUserRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.COOKIES.get('my_cookie') == 'cookie_value':
            return super().dispatch(request, *args, **kwargs) # triggers the dispatch from TemplateView, 
                                                                # because TemplateView comes after the Mixin in the MRO
        return HttpResponseForbidden('You are not allowed') 

class AboutPageView(ActiveUserRequiredMixin, TemplateView):
    template_name = "about.html"
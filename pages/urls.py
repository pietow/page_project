from django.urls import path
from .views import home_page_view, HomePageView2, AboutPageView

urlpatterns = [
    path('', home_page_view, name='home'),
    # path('', HomePageView2.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
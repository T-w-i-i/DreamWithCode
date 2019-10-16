from django.urls import path
from .views import HomeView, AboutView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'dwcsite'

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('about', AboutView.as_view(), name = 'about'),
]

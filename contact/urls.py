from django.urls import path
from. views import ContactView, SentView

app_name = 'contact'
urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('sent/', SentView.as_view(), name='sent'),
]
from django.urls import path
from .views import ExhibitionListView

app_name = 'show'
urlpatterns = [
    path('', ExhibitionListView.as_view(), name='exhibitions'),
]
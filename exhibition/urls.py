from django.urls import path
from .views import ExhibitionListView

app_name = 'exhibition'
urlpatterns = [
    path('', ExhibitionListView.as_view(), name='exhibitions'),
]
from django.urls import path, include

from .views import PaintingListView, PaintingYearArchiveView, PaintingArchiveIndexView
from .models import Painting

app_name = 'work'
urlpatterns = [
    path('', PaintingArchiveIndexView.as_view(), name='painting_archive'),
    path('<int:year>/', PaintingYearArchiveView.as_view(), name='painting_archive_year'),
]
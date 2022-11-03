from django.views.generic import ListView
from django.views.generic import ArchiveIndexView, YearArchiveView

from .models import Painting, MainPainting



class MainPaintingView(ListView):
    model = MainPainting
    context_object_name = 'main'

class PaintingListView(ListView):
    model = Painting
    context_object_name = 'paintings'
    
    
class PaintingArchiveIndexView(ArchiveIndexView):
    model = Painting
    date_field = 'date'



class PaintingYearArchiveView(YearArchiveView):
    model = Painting
    date_field = 'date'
    make_object_list = True
    

from django.views.generic import ListView
from .models import Exhibition

class ExhibitionListView(ListView):
    queryset = Exhibition.objects.all().order_by('start_date')
    context_object_name = 'exhibitions'
    template_name = 'exhibition/exhibitions.html'
from django.http import HttpResponse

from .models import Busine


def index(request):
    latest_busines_list = Busine.objects.order_by("-name")[:5]
    output = ", ".join([q.name for q in latest_busines_list])
    return HttpResponse(output)

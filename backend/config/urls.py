from django.urls import path
from django.http import HttpResponse


def health(request):
    return HttpResponse('ERP.SAAD API OK')

urlpatterns = [
    path('', health),
]

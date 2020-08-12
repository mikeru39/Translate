from django.shortcuts import render

# Create your views here.
from example.models import Course


def index(request):
    course = Course.objects.all()
    return render(request, 'example/index.html', {'course': course})

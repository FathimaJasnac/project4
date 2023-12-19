from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# Create your views here.
def demo(request):
     # fetch table elements
     obj=Place.objects.all()
     obj1=Team.objects.all()
     return render(request,"index.html",{'result':obj,'res':obj1})


from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def student_valid(request):
    s=studentform()
    d={'s':s}
    if request.method=='POST':
        sf=studentform(request.POST)
        if sf.is_valid():
            return HttpResponse(str(sf.cleaned_data))
        else:
            return HttpResponse('<h1 style="color:blue;">invalid data</h1>')




    return render(request,'student_valid.html',d)
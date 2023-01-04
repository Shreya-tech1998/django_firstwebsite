from django.shortcuts import render
from .models import about,slider

# Create your views here.
def home(request):
    objectdata = about.objects.all()
    sliderdata = slider.objects.all()
    context = {
        'about':objectdata,
        'slider':sliderdata
    }
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,'about.html')





from django.shortcuts import render

# Create your views here.

def about(request):
    datas={

    }
    return render(request,'pages/About/about.html')

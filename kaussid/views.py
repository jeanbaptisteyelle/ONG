from django.shortcuts import render

# Create your views here.
def causes(request):
    datas={

    }
    return render(request,'pages/Kaussid/causes.html')

def cause_single(request):
    datas={

    }
    return render(request,'pages/Kaussid/cause-single.html')

def donate(request):
    datas={

    }
    return render(request,'pages/Kaussid/donate.html')

def events(request):
    datas={

    }
    return render(request,'pages/Kaussid/events.html')

def event_single(request):
    datas={

    }
    return render(request,'pages/Kaussid/event-single.html')

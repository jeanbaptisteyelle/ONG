from django.shortcuts import render

# Create your views here.
def blog(request):
    datas={

    }
    return render(request,'pages/Blog/blog.html')


def volunteers(request):
    datas={

    }
    return render(request,'pages/Blog/volunteers.html')

def blog_single(request):
    datas={

    }
    return render(request,'pages/Blog/blog-single.html')

def faq(request):
    datas={

    }
    return render(request,'pages/Blog/faq.html')


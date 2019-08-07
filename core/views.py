from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'hello':'hello world',
         'pj':'poli junior',
    }

    return render(request,'core/index.html',context)